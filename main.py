from fastapi import FastAPI, APIRouter
from app.routers import anoncreds, registry, resolver, vc_api, converter
from app.metadata import tags_metadata
from config import settings

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
    return settings.DID_DOC

api_router.include_router(registry.router)
api_router.include_router(resolver.router)
api_router.include_router(anoncreds.router)
api_router.include_router(converter.router)
api_router.include_router(vc_api.router)

app.include_router(api_router)
