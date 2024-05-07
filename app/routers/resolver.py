from fastapi import APIRouter, Body, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from config import settings
# from app.models import 
import json
import base64
import requests
from pprint import pprint
from datetime import datetime

router = APIRouter()

@router.get("/resolve/{ressourceId}", tags=["Resolver"], summary="Resolve AnonCreds Ressource")
async def create_schema(ressourceId: str):
    ressource_id = ressourceId
    did = ressource_id.split("?")[0]
    r = requests.get(f'https://uniresolver.dtt-dev.idlab.app/1.0/identifiers/{did}')
    did_doc = r.json()
    print(did_doc)
    
    
    # query = ressource_id.split("?")[-1]
    # service_type = query.split('&')[0]
    # service_type = service_type.split('=')[-1]
    # path = query.split('&')[-1]
    # path = query.split('=')[-1]
    # ressource = {}
    # return {"ressource": ressource}