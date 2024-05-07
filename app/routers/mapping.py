from fastapi import APIRouter, Body, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from config import settings
from app.models import MapToAnonCredsRequest, MapToW3CRequest
from app.controllers import anoncreds
import json
import base64
from pprint import pprint
from datetime import datetime

router = APIRouter()

@router.post(
    "/mapping/w3c-to-anon", 
    tags=["Mapping"], 
    summary="Map a Credential to a supported format (w3c)"
)
async def map_credential(request_body: MapToAnonCredsRequest):
    credential = vars(request_body)['credential']
    credential = anoncreds.map_to_anoncreds(credential)
    return credential

@router.post(
    "/mapping/anon-to-w3c", 
    tags=["Mapping"], 
    summary="Map a Credential to a supported format (w3c)"
)
async def map_credential(request_body: MapToW3CRequest):
    credential = vars(request_body)['credential']
    credential = anoncreds.map_to_w3c(credential)
    return credential

# @router.post(
#     "/mapping/presentation", 
#     tags=["Mapping"], 
#     summary="Map a Presentation to a supported format (w3c)"
# )
# async def map_presentation(schema: CredentialsMapBody):
#     return ""