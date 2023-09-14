from fastapi import APIRouter, Body, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from config import settings
from app.models import CredentialsMapBody
import json
import base64
from pprint import pprint
from datetime import datetime

router = APIRouter()

@router.post(
    "/conversion/credential/<output_format>", 
    tags=["Conversion"], 
    summary="Map a Credential to a supported format (w3c)"
)
async def post_schema(schema: CredentialsMapBody):
    return ""

@router.post(
    "/conversion/presentation/<output_format>", 
    tags=["Conversion"], 
    summary="Map a Presentation to a supported format (w3c)"
)
async def post_schema(schema: CredentialsMapBody):
    return ""