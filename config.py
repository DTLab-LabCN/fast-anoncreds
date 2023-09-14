from pydantic import BaseSettings
import os
from dotenv import load_dotenv

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
    DID_DOC = {
        "@context": [
            "https://www.w3.org/ns/did/v1",
            "https://w3id.org/security/suites/jws-2020/v1"
        ],
        "id":f"did:web:{DOMAIN}",
        "verificationMethod": [
            {
            "id": f"did:web:{DOMAIN}#key-1",
            "type": "JsonWebKey2020",
            "controller": f"did:web:{DOMAIN}",
            "publicKeyJwk": {
                "crv": "Ed25519",
                "kty": "OKP",
                "x": os.environ["PUBLIC_JWK"]
            }
            }
        ],
        "service": [
            {
                "id": f"did:web:{DOMAIN}#registry",
                "type": "AnonCredsRegistry",
                "serviceEndpoint": f"https://{DOMAIN}/registry"
            }
        ]
    }

settings = Settings()
