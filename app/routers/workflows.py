from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from config import settings
from app.models import CredentialOfferRequest
from anoncreds import CredentialOffer

router = APIRouter()


@router.post(
    "/workflows/issuance", 
    tags=["Workflows"], 
    summary="Create Credential Offer"
)
async def credential_offer(request: CredentialOfferRequest):
    cred_def_id = request['credDefId']
    schema_id = ''
    cred_def_correctness = ''
    cred_offer = CredentialOffer.create(schema_id, cred_def_id, cred_def_correctness)
    return cred_offer


@router.post(
    "/workflows/presentation", 
    tags=["Workflows"], 
    summary="Create Presentation Request"
)
async def credential_offer(request: CredentialOfferRequest):
    cred_def_id = request['credDefId']
    schema_id = ''
    cred_def_correctness = ''
    cred_offer = CredentialOffer.create(schema_id, cred_def_id, cred_def_correctness)
    return cred_offer


@router.get(
    "/workflows/{workflowId}/exchanges/{exchangeId}", 
    tags=["Workflows"], 
    summary="Workflow exchange"
)
async def get_workflow_exchange(workflowId: str, exchangeId: str):
    return ''


@router.post(
    "/workflows/{workflowId}/exchanges/{exchangeId}", 
    tags=["Workflows"], 
    summary="Workflow exchange"
)
async def post_workflow_exchange(workflowId: str, exchangeId: str, request: Request):
    return ''

# @router.post(
#     "/issuance/request", 
#     tags=["Issuance"], 
#     summary="Create Credential Request"
# )
# async def issuance_request(request: IssuanceRequestBody):
#     link_secret_id = request['linkSecretId']
#     link_secret = ''
#     cred_offer = request['credentialOffer']
#     cred_def_id = cred_offer['cred_def_id']
#     cred_def_pub = {}
#     entropy = str(uuid4())
#     cred_request, cred_request_metadata = CredentialRequest.create(
#         entropy, None, cred_def_pub, link_secret, link_secret_id, cred_offer
#     )
#     return cred_request

# @router.post(
#     "/issuance/issue", 
#     tags=["Issuance"], 
#     summary="Issue Credential"
# )
# async def issuance_issue(request: IssuanceCredentialBody):
#     credential = request['credential']
#     cred_request = request['credentialRequest']
#     cred_def_id = cred_request['cred_def_id']
#     cred_def_pub = {}
#     cred_def_priv = {}
#     cred_offer = {}
#     rev_reg_def_pub = {}
#     rev_reg_def_private = {}
#     revocation_status_list = {}
#     rev_idx = 4
#     issue_cred = W3cCredential.create(
#         cred_def_pub,
#         cred_def_priv,
#         cred_offer,
#         cred_request,
#         credential['credentialSubject'],
#         CredentialRevocationConfig(
#             rev_reg_def_pub,
#             rev_reg_def_private,
#             revocation_status_list,
#             rev_idx,
#         ),
#         None,
#     )

#     # recv_cred = issue_cred.process(
#     #     cred_request_metadata, link_secret, cred_def_pub, rev_reg_def_pub
#     # )
#     return issue_cred

# @router.post(
#     "/issuance/verify", 
#     tags=["Issuance"], 
#     summary="Verify Credential"
# )
# async def issuance_verify(schema: IssuanceCredentialBody):
#     return ""

# @router.post(
#     "/presentation/request", 
#     tags=["Presentation"], 
#     summary="Create Presentation Request"
# )
# async def presentation_request(schema: PresentationBody):
#     return ""

# @router.post(
#     "/presentation/generate", 
#     tags=["Presentation"], 
#     summary="Generate Presentation"
# )
# async def presentation_prove(schema: PresentationBody):
#     return ""

# @router.post(
#     "/presentation/verify", 
#     tags=["Presentation"], 
#     summary="Verify Presentation"
# )
# async def presentation_verify(schema: PresentationBody):
#     return ""

# @router.post(
#     "/revocation/revoke", 
#     tags=["Revocation"], 
#     summary="Revoke Credential"
# )
# async def revocation_revoke(schema: RevocationBody):
#     return ""