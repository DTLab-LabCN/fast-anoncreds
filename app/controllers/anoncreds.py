from anoncreds import (
    create_link_secret,
    Schema,
    Credential,
    CredentialDefinition,
    CredentialOffer,
    CredentialRequest,
    W3cCredential
)
# from app.controllers import agent
import uuid
from config import settings

# def schema_from_id(schema_id):
#     schema = agent.get_schema(schema_id)
#     schema = Schema.create(
#         schema['name'], schema['version'], schema['id'].split(':')[0], schema['attrNames']
#     )
#     return schema
    
def create_cred_def(schema_id, schema, issuer, tag):
    cred_def_pub, cred_def_priv, cred_def_correctness = CredentialDefinition.create(
        schema_id, schema, issuer, tag, "CL", support_revocation=False
    )
    return cred_def_pub, cred_def_priv, cred_def_correctness

def self_issuance(credential):
    credential_id = str(uuid.uuid4())
    schema_name = credential['credentialSubject']['type'][0]
    schema_version = '1.0'
    issuer = settings.DID_WEB_BASE
    attributes = credential['credentialSubject'].copy()
    attributes.pop('type')
    attributes_list = [attribute for attribute in attributes]
    schema = Schema.create(
        schema_name, schema_version, issuer, attributes_list
    )
    
    schema_query = f'?service=AnonCredsRegistry&relativeRef=/schemas/{schema_name}/{schema_version}'
    schema_id = issuer+schema_query
    cred_def_tag = str(uuid.uuid4())
    cred_def_pub, cred_def_priv, cred_def_correctness = CredentialDefinition.create(
        schema_id, schema, issuer, cred_def_tag, "CL", support_revocation=False
    )
    
    cred_def_query = f'?service=AnonCredsRegistry&relativeRef=/cred_defs/{cred_def_tag}'
    cred_def_id = issuer+cred_def_query
    cred_offer = CredentialOffer.create(schema_id, cred_def_id, cred_def_correctness)
    link_secret = create_link_secret()
    link_secret_id = str(uuid.uuid4())
    entropy = str(uuid.uuid4())
    cred_request, cred_request_metadata = CredentialRequest.create(
        entropy, None, cred_def_pub, link_secret, link_secret_id, cred_offer
    )
    credential = W3cCredential.create(
        cred_def_pub,
        cred_def_priv,
        cred_offer,
        cred_request,
        attributes,
        None,
        None,
    )
    # credential = credential.to_legacy()
    # credential = Credential.create(
    #     cred_def_pub,
    #     cred_def_priv,
    #     cred_offer,
    #     cred_request,
    #     attributes,
    #     None,
    #     None,
    # )
    
    return credential.to_dict()

def map_to_anoncreds(credential):
    credential = W3cCredential.load(credential)
    credential = credential.to_legacy()
    return credential.to_dict()

def map_to_w3c(credential):
    issuer = credential['cred_def_id'].split('?')[0]
    credential = Credential.load(credential)
    credential = W3cCredential.from_legacy(credential, issuer)
    return credential.to_dict()