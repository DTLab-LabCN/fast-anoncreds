from typing import Union, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from config import settings

class SetupSchemaBody(BaseModel):
    schema_input: dict = Field(alias='schema', example={
        "name": "DemoSchema",
        "attributes": ["DemoAttr_1", "DemoAttr_2"]
    })
    options: dict = Field(example={
        # "method": "web",
        # "service": False
    })

class SetupCredDefBody(BaseModel):
    cred_def_input: dict = Field(alias='cred_def', example={
        "label": "DemoCredential",
        "schema": {
            "id": f"did:web:{settings.DOMAIN}#DemoSchema"
        },
        # "revocation": False
    })
    options: dict = Field(example={
        # "method": "web",
        # "service": False
    })

class IssuanceBody(BaseModel):
    schema_input: dict = Field(alias='credentialSchema', example={
        "id": f"did:web:{settings.DOMAIN}#z<>",
        "schema": f"did:web:{settings.DOMAIN}#DemoSchema"
    })
    values: dict = Field(alias='credentialSubject', example={
        "DemoAttr_1": "DemoValue_1",
        "DemoAttr_2": "DemoValue_2",
    })
    options: dict = Field(example={})

class IssuanceOfferBody(BaseModel):
    cred_def_id: dict = Field(alias='cred_def', example={
        "id": f"did:web:{settings.DOMAIN}#z<>"
    })
    options: dict = Field(example={})

class IssuanceRequestBody(BaseModel):
    offer: dict = Field(alias='offer', example={
        "nonce": "",
        "schema_id": f"did:web:{settings.DOMAIN}#DemoSchema",
        "cred_def_id": f"did:web:{settings.DOMAIN}#z<>",
        "key_proof": {
            "c": "",
            "xz_cap": "",
            "xr_cap": [
                [
                    "master_secret",
                    ""
                ],
                [
                    "DemoAttr_1",
                    ""
                ],
                [
                    "DemoAttr_2",
                    ""
                ]
            ]
        },
    })
    options: dict = Field(example={})

class IssuanceCredentialBody(BaseModel):
    request: dict = Field(alias='request', example={
            "nonce": "",
            "entropy": "",
            "cred_def_id": f"did:web:{settings.DOMAIN}#z<>",
            "blinded_ms": {
                "u": "",
                "ur": "null",
                "hidden_attributes": [
                    "master_secret"
                ],
                "committed_attributes": {}
            },
            "blinded_ms_correctness_proof": {
                "c": "",
                "v_dash_cap": "",
                "m_caps": {
                    "master_secret": ""
                },
                "r_caps": {}
            }
        })
    options: dict = Field(example={})

class PresentationBody(BaseModel):
    request: dict = Field(alias='presentationRequest', example={
        "name": "DemoPresentationRequest",
        "attributes": {},
        "predicates": {},
    })
    options: dict = Field(example={
        "nonce": "",
        "version": "",
        "non_revoked": ""
    })

class PresentationRequestBody(BaseModel):
    offer: dict = Field(alias='offer', example={
        "cred_def_id": f"did:web:{settings.DOMAIN}#z<>",
        "schema_id": f"did:web:{settings.DOMAIN}#DemoSchema",
        "key_proof": {

        },
    })
    options: dict = Field(example={})

class PresentationResponseBody(BaseModel):
    request: dict = Field(alias='request', example={
        "cred_def_id": f"did:web:{settings.DOMAIN}#z<>",
        "schema_id": f"did:web:{settings.DOMAIN}#DemoSchema",
        "key_proof": {
            
        },
    })
    options: dict = Field(example={})

class RevocationBody(BaseModel):
    options: dict = Field(example={})

# class CredentialsRequestBody(BaseModel):
#     offer: dict = Field(alias='credentialOffer', example={
#         "@context": [
#             "https://www.w3.org/2018/credentials/v1",
#             "https://andrewwhitehead.github.io/anoncreds-w3c-mapping/schema.json",
#             {
#             "@vocab": "urn:anoncreds:attributes#"
#             }
#         ],
#         "issuer": f"did:web:{settings.DOMAIN}",
#         "validFrom": "",
#         "type": [
#             "VerifiableCredential",
#             "AnonCredsCredential",
#         ],
#         "credentialSchema": {
#             "id": f"did:web:{settings.DOMAIN}#z<>",
#             "schema": f"did:web:{settings.DOMAIN}#DemoSchema"
#         },
#         "proof": {
#             "c": "103...961",
#             "xz_cap": "563...205",
#             "xr_cap": [
#                 [
#                     "master_secret",
#                     "156...104"
#                 ],
#                 [
#                     "UID",
#                     "821...452"
#                 ],
#                 [
#                     "EMAIL",
#                     "196...694"
#                 ],
#                 [
#                     "ORG",
#                     "196...694"
#                 ],
#                 [
#                     "KEY",
#                     "196...694"
#                 ]
#             ]
#         },
#     })
#     options: dict = Field(example={})

class CredentialsIssueBody(BaseModel):
    credential: dict = Field(alias='credential', example={
        "@context": [
            "https://www.w3.org/2018/credentials/v1",
            "https://andrewwhitehead.github.io/anoncreds-w3c-mapping/schema.json",
            {
            "@vocab": "urn:anoncreds:attributes#"
            }
        ],
        "issuer": f"did:web:{settings.DOMAIN}",
        "validFrom": datetime.now(),
        # "validUntil": "null",
        "type": [
            "VerifiableCredential",
            "AnonCredsCredential",
        ],
        "credentialSchema": {
            "id": f"did:web:{settings.DOMAIN}?service=registry&relativeRef=/credDef/z<>",
            "schema": f"did:web:{settings.DOMAIN}?service=registry&relativeRef=/schema/z<>"
        },
        "credentialSubject": {
            "DemoAttr_1": "DemoValue_1",
            "DemoAttr_2": "DemoValue_2"
        },
        "credentialStatus": {
            "type": "AnonCredsRevocation",
            "id": f"did:web:{settings.DOMAIN}?service=registry&relativeRef=/revReg/z<>", 
        }
    })
    options: dict = Field(example={
        "entropy": "",
        "blinded_ms": {
            "u": "",
            "ur": "null",
            "hidden_attributes": [
                "master_secret"
            ],
            "committed_attributes": {}
        },
        "blinded_ms_correctness_proof": {
            "c": "",
            "v_dash_cap": "",
            "m_caps": {
                "master_secret": ""
            },
            "r_caps": {}
        }
        })


class CredentialsMapBody(BaseModel):
    credential: dict = Field(alias='credential', example={
        "@context": [
            "https://www.w3.org/2018/credentials/v1",
            "https://andrewwhitehead.github.io/anoncreds-w3c-mapping/schema.json",
            {
            "@vocab": "urn:anoncreds:attributes#"
            }
        ],
        "issuer": f"did:web:{settings.DOMAIN}",
        "validFrom": "",
        "type": [
            "VerifiableCredential",
            "AnonCredsCredential",
        ],
        "credentialSchema": {
            "id": f"did:web:{settings.DOMAIN}#z<>",
            "schema": f"did:web:{settings.DOMAIN}#DemoSchema"
        },
        "credentialSubject": {
        },
        "credentialStatus": {
            "type": "AnonCredsRevocation",
            "id": f"did:web:{settings.DOMAIN}#z<>", 
        },
        "proof": {}
    })
    options: dict = Field(example={
        "input": "w3c",
        "output": "anoncreds",
    })