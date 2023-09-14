from fastapi import APIRouter, Body, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from config import settings
from app.models import (
    SetupSchemaBody, SetupCredDefBody, 
    IssuanceOfferBody, IssuanceRequestBody, IssuanceCredentialBody,
    PresentationBody, PresentationResponseBody,
    RevocationBody
    )
import json
import base64
from pprint import pprint
from datetime import datetime

router = APIRouter()

@router.post("/setup/link", tags=["Setup"], summary="Create Link Secret")
async def setup_link(schema: SetupSchemaBody):
    return ""

@router.post("/setup/schema", tags=["Setup"], summary="Publish Schema")
async def setup_schema(schema: SetupSchemaBody):
    return ""

@router.post("/setup/definition", tags=["Setup"], summary="Publish Credential Definition")
async def setup_cred_def(schema: SetupCredDefBody):
    return ""

@router.post(
    "/setup/revocation", 
    tags=["Setup"], 
    summary="Publish Revocation Registry"
)
async def setup_revocation(schema: SetupCredDefBody):
    return ""

@router.post(
    "/issuance/offer", 
    tags=["Issuance"], 
    summary="Create Credential Offer"
)
async def issuance_offer(schema: IssuanceOfferBody):
    return ""

@router.post(
    "/issuance/request", 
    tags=["Issuance"], 
    summary="Create Credential Request"
)
async def issuance_request(schema: IssuanceRequestBody):
    return ""

@router.post(
    "/issuance/issue", 
    tags=["Issuance"], 
    summary="Issue Credential"
)
async def issuance_issue(schema: IssuanceCredentialBody):
    return ""

@router.post(
    "/issuance/verify", 
    tags=["Issuance"], 
    summary="Verify Credential"
)
async def issuance_verify(schema: IssuanceCredentialBody):
    return ""

@router.post(
    "/presentation/request", 
    tags=["Presentation"], 
    summary="Create Presentation Request"
)
async def presentation_request(schema: PresentationBody):
    return ""

@router.post(
    "/presentation/generate", 
    tags=["Presentation"], 
    summary="Generate Presentation"
)
async def presentation_prove(schema: PresentationBody):
    return ""

@router.post(
    "/presentation/verify", 
    tags=["Presentation"], 
    summary="Verify Presentation"
)
async def presentation_verify(schema: PresentationBody):
    return ""

@router.post(
    "/revocation/revoke", 
    tags=["Revocation"], 
    summary="Revoke Credential"
)
async def revocation_revoke(schema: RevocationBody):
    return ""