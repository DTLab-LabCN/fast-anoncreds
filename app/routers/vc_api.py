from fastapi import APIRouter, Body, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from config import settings
from app.models import CredentialsIssueBody
import json
import base64
from pprint import pprint
from datetime import datetime

router = APIRouter()

# @router.post(
#     "/credentials/request", 
#     tags=["VC-API"], 
#     summary="[Experimental] Request VC"
# )
# async def post_schema(schema: CredentialsRequestBody):
#     return ""

@router.post(
    "/credentials/issue", 
    tags=["VC-API"], 
    summary="Issue VC"
)
async def post_schema(schema: CredentialsIssueBody):
    return ""

@router.post(
    "/credentials/verify", 
    tags=["VC-API"], 
    summary="Verify VC"
)
async def post_schema(schema: CredentialsIssueBody):
    return ""

# @router.post(
#     "/presentations/request", 
#     tags=["VC-API"], 
#     summary="[Experimental] Request Presentation"
# )
# async def post_schema(schema: CredentialsIssueBody):
#     return ""

@router.post(
    "/presentations/prove", 
    tags=["VC-API"], 
    summary="Generate Presentation"
)
async def post_schema(schema: CredentialsIssueBody):
    return ""

@router.post(
    "/presentations/verify", 
    tags=["VC-API"], 
    summary="Verify Presentation"
)
async def post_schema(schema: CredentialsIssueBody):
    return ""