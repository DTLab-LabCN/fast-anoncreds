from fastapi import FastAPI, APIRouter
# from fastapi.responses import JSONResponse
from app.routers import registry, resolver, vc_api, mapping, workflows
# from app.validations import ValidationException
from config import settings
import asyncio

app = FastAPI(
    title=settings.PROJECT_TITLE,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    contact=settings.PROJECT_CONTACT,
    license_info=settings.PROJECT_LICENSE_INFO,
)


api_router = APIRouter()

@api_router.get(
    "/.well-known/did.json", 
    tags=["WellKnownDID"], 
    summary="Well-known DID"
)
async def well_known_did():
    did_doc = {
        "@context": [
            "https://www.w3.org/ns/did/v1"
        ],
        "id": settings.HTTPS_BASE,
        "service": [
            {
            "id": "#anoncreds-registry",
            "type": "AnonCredsRegistry",
            "serviceEndpoint": f'{settings.HTTPS_BASE}/anoncreds'
            }
        ],
        "verificationMethod": [],
        "authentication": [],
        "assertionMethod": []
        }
    return did_doc

api_router.include_router(resolver.router)
api_router.include_router(registry.router)
api_router.include_router(workflows.router)
api_router.include_router(vc_api.router)
api_router.include_router(mapping.router)

# api_router.include_router(registry.router)
# api_router.include_router(resolver.router)
# api_router.include_router(converter.router)

app.include_router(api_router)
