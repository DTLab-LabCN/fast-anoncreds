from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config import settings
from app.models import CreateSchemaRequest, CreateCredDefRequest
from app.controllers import askar
import uuid
from anoncreds import Schema, CredentialDefinition

router = APIRouter()

@router.post("/anoncreds/schemas", tags=["Registry"], summary="Create Schema")
async def create_schema(request: CreateSchemaRequest):
    name = vars(request)['name']
    version = vars(request)['version']
    attributes = vars(request)['attributes']
    issuer = settings.DID_WEB_BASE
    schema = Schema.create(
        name, version, issuer, attributes
    )
    schema = schema.to_dict()
    schema_query = f'?service=AnonCredsRegistry&relativeRef=/schemas/{name}/{version}'
    schema_id = issuer+schema_query
    try:
        data_key = f'registry:schemas:{name}:{version}'
        await askar.store_data(settings.ASKAR_KEY, data_key, schema)
        return {"schema_id": schema_id}
    except:
        return JSONResponse(content=f'Schema {schema_id} already exists')

@router.get("/anoncreds/schemas/{schemaName}/{schemaVersion}", tags=["Registry"], summary="Get Schema")
async def get_schema(schemaName: str, schemaVersion: str):
    schema_name = schemaName
    schema_version = schemaVersion
    try:
        data_key = f'registry:schemas:{schema_name}:{schema_version}'
        schema = await askar.fetch_data(settings.ASKAR_KEY, data_key)
        return {"schema": schema}
    except:
        return JSONResponse(content='Schema not found')

@router.post("/anoncreds/definitions", tags=["Registry"], summary="Create Credential Definition")
async def create_cred_def(request: CreateCredDefRequest):
    schema_id = vars(request)['schema_id']
    tag = str(uuid.uuid4)
    issuer = settings.DID_WEB_BASE
    schema = {}
    cred_def_pub, cred_def_priv, cred_def_correctness = CredentialDefinition.create(
        schema_id, schema, issuer, tag, "CL", support_revocation=False
    )
    cred_def_query = f'?service=AnonCredsRegistry&relativeRef=/definitions/{tag}'
    cred_def_id = issuer+cred_def_query
    return {"cred_def_id": cred_def_id}

@router.get("/anoncreds/definitions/{credDefTag}", tags=["Registry"], summary="Get Credential Definition")
async def create_schema(credDefTag: str):
    cred_def_tag = credDefTag
    data_key = f'registry:definitions:{cred_def_tag}'
    cred_def = {}
    return {"cred_def": cred_def}
