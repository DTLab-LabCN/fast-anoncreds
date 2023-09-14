from fastapi import APIRouter, Body, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from config import settings
# from app.models import 
import json
import base64
from pprint import pprint
from datetime import datetime

router = APIRouter()

@router.get(
    "/resolve/<method>/<object_id>",
    tags=["Resolver"], 
    summary="Resolve a URL encoded AnonCreds Object ID from a given method (web, sov, indy, cheqD, cardano)"
)
async def get_object(hash):
    return ""