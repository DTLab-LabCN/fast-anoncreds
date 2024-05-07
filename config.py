from pydantic import BaseSettings
import os
from dotenv import load_dotenv
from aries_askar.bindings import generate_raw_key

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Settings(BaseSettings):
    PROJECT_TITLE = "FastAnonCreds"
    PROJECT_VERSION = "v0"
    PROJECT_DESCRIPTION = """
    FastAPI implementation of the AnonCreds-rs Python Wrapper
    Specifications:
    - AnonCreds v1.0
    - DID Core v1.0
    - DID Web
    - VC-API v0.3
    - Verifiable Credential Data Model v2.0
    """
    PROJECT_CONTACT = {
        "name": "IDLab",
        "url": "https://github.com/IDLab-org/fast-anoncreds",
    }
    PROJECT_LICENSE_INFO = {
        "name": "Apache License",
        "url": "http://www.apache.org/licenses/",
    }

    DOMAIN = os.environ['DOMAIN']
    DID_WEB_BASE: str = f"did:web:{DOMAIN}"
    HTTPS_BASE: str = f"https://{DOMAIN}"
    
    ASKAR_KEY: str = generate_raw_key(os.environ["ASKAR_SEED"])
    
    POSTGRES_URI: str = os.environ["POSTGRES_URI"]

settings = Settings()
