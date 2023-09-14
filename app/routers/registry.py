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

# @router.get(
#     "/registry",
#     tags=["Registry"], 
#     summary="Fetch Object"
# )
# async def get_object():
#     return ""

@router.get(
    "/registry/<object_type>/<object_hash>",
    tags=["Registry"], 
    summary="Fetch AnonCreds Object (Schema, CredDef, RevRegDef, RevReg)"
)
async def get_object():
    return ""

# @router.post(
#     "/registry",
#     tags=["Registry"], 
#     summary="Store Object"
# )
# async def store_object():
#     return ""

# @router.delete(
#     "/registry",
#     tags=["Registry"], 
#     summary="Remove Object"
# )
# async def delete_object():
#     return ""