from typing import Union, Optional, List, Dict
from pydantic import BaseModel, Field
from datetime import datetime
from config import settings

class CreateSchemaRequest(BaseModel):
    name: str = Field(example='MovieTicket')
    version: str = Field(example='1.0')
    attributes: List[str] = Field(example=['movieTitle', 'movieRoom', 'movieTime'])

class CreateCredDefRequest(BaseModel):
    schema_id: str = Field(example=f'{settings.DID_WEB_BASE}?service=AnonCredsRegistry&relativeRef=/schemas/MovieTicket/1.0')

class CredentialOfferRequest(BaseModel):
    credential: Dict = Field(example={
            '@context': [],
            'type': ['VerifiableCredential', 'MovieTicketCredential'],
            'issuer': '',
            'credentialSubject': {
                'type': ['MovieTicket'],
                'movieTitle': 'Planet of the Apes',
                'movieRoom': 'G2',
                'movieTime': '11:18',
                },
            'issuanceDate': '',
            'expirationDate': ''
        })
    options: Dict = Field(example={
        'verificationMethod': f'{settings.DID_WEB_BASE}?service=AnonCredsRegistry&relativeRef=/definitions/abc'
    })
    
class MapToW3CRequest(BaseModel):
    credential: dict = Field(example={
        "schema_id": "did:web:anoncreds.opsec.id?service=AnonCredsRegistry&relativeRef=/schemas/Person/1.0",
        "cred_def_id": "did:web:anoncreds.opsec.id?service=AnonCredsRegistry&relativeRef=/cred_defs/f6ff4667-299b-4332-b360-bf9bde980edb",
        "rev_reg_id": None,
        "values": {
            "lastName": {
            "raw": "Jones",
            "encoded": "114927502338763998064999850638882995061695907387154193658986605318642155271625"
            },
            "firstName": {
            "raw": "Alice",
            "encoded": "27034640024117331033063128044004318218486816931520886405535659934417438781507"
            }
        },
        "signature": {
            "p_credential": {
            "m_2": "15697238325406143657212625157154512104650701814931317913907163684484005199819",
            "a": "58985551687792775613776389735378876426447095917185650463294290745427237647224878066884195807671086267663511951152385777343428649611280968632717206768434107532068646902626702383399229671738472665026386280786861429123616316393244812779507626193587717419226731885386464338028532900498383583191409784293607307229339634659204317712094447982923020212381983258941810942427402668910264505440668269853997488086005966816984297596240810878525084992109418714222312994092705336723618067881306185945126572921070889296712615132453914798279471214661143771829239786189604930088237197148286124148986128791462063818473159070553217498952",
            "e": "259344723055062059907025491480697571938277889515152306249728583105665800713306759149981690559193987143012367913206299323899696942213235956742930180498441379700238292763651178182269",
            "v": "6161542956840530963033337872419424141551184225652204947382667009020285566229996151946773705556509874679336600908544482327850292130121645639336177704249463505562032563457890574379520130866438070166469109325849092584321935331416189616015767616000815915092124196793505617847938827683275014579969591325131844248524577996288368714034100838317361288805334902431080079012417714367885749468980687147338708807504755944298552707587142856222100156116586494313418560646220312934166894447609898201263784514072735860641963152197825297756169566612362378720003780471695537707648890652571734628079609875552038892759471456347328936346605784196198770777248693925625509889967443876995155433923350300095999906893122094042304960562662065832169531830876661655545126696364232717461348215315357827594230180281633666782866561685974338220286127538"
            },
            "r_credential": None
        },
        "signature_correctness_proof": {
            "se": "9018539471096487215621206138285736476260455045242159974923925039107514529427939603887282340719708830090519847759922784209972991958271453280500607923999425213022382802552508315265852574468267598726947365420039085240769731452586636418555084886622159069679667027650954837219027224921224340628194182386127234631091065941054869712502457355391369646138199918100670930785423315513955348838192145593513961614454862414805771267144753633073558576689664243601576777714118891433311010041411170650025601335919111492098381165205214259202907206631017632629991789142058422407251451300994351750211407567382540900567790548857843352066",
            "c": "59966147424798324329562582651672500734402322481246693604523475679929969956151"
        },
        "rev_reg": None,
        "witness": None
        })
    
class MapToAnonCredsRequest(BaseModel):
    credential: dict = Field(example={
            "@context": [
                "https://www.w3.org/2018/credentials/v1",
                "https://w3id.org/security/data-integrity/v2",
                {
                "@vocab": "https://www.w3.org/ns/credentials/issuer-dependent#"
                }
            ],
            "type": [
                "VerifiableCredential"
            ],
            "issuer": "did:web:anoncreds.opsec.id",
            "credentialSubject": {
                "firstName": "Alice",
            },
            "proof": [
                {
                "type": "DataIntegrityProof",
                "cryptosuite": "anoncredsvc-2023",
                "proofPurpose": "assertionMethod",
                "verificationMethod": "did:web:anoncreds.opsec.id?service=AnonCredsRegistry&relativeRef=/cred_defs/f6ff4667-299b-4332-b360-bf9bde980edb",
                "proofValue": "uhKlzY2hlbWFfaWTZVGRpZDp3ZWI6YW5vbmNyZWRzLm9wc2VjLmlkP3NlcnZpY2U9QW5vbkNyZWRzUmVnaXN0cnkmcmVsYXRpdmVSZWY9L3NjaGVtYXMvUGVyc29uLzEuMKtjcmVkX2RlZl9pZNlwZGlkOndlYjphbm9uY3JlZHMub3BzZWMuaWQ_c2VydmljZT1Bbm9uQ3JlZHNSZWdpc3RyeSZyZWxhdGl2ZVJlZj0vY3JlZF9kZWZzL2Y2ZmY0NjY3LTI5OWItNDMzMi1iMzYwLWJmOWJkZTk4MGVkYqlzaWduYXR1cmWCrHBfY3JlZGVudGlhbISjbV8y3AAgIsy0UnF0OyvMlMztbMz9zIgZJczgzMLM38yIzMXM7zt1QlnM-FjMvsz2YUt_zMuhYdwBAQHM00FtUcyHzK3Mh8ykzN3MsMzjzMTM8szEzJ7Mw8zrzOtkfkzM9cyDzMPM28zhXx7MgnQzZszMzJHM7hTM7SZSzIpSOszXzO_M0cyiSMyRzKBJzJfMx8yEzMrMgsykcszKRQ7M3szHJ8zzzJFKzKRMzJ8MzLEnzIAGzMbMysziBAYkzPg7zNsCKxXM-wrM-kNjeFHMlT4zzPDMmsykzMJ0zPUOzLB9zNzMo8yqzP81zN5mzInMt2xAAxxnzIDM9R10QC8ZY0ZMzM_MwHdmWElzPj92zOtALszmzI59fyBJRGAcIj3MxxjM9Mz4ciDMziIvzMJJzP4hRDnM5n3Myn5fRMyEzK7MwTQnzIPMgczpZn5HExrMz0EgzJF4zLrMrMyMzKhizJnMs1FozOnMzxXM2mfMm3VVzK7M1szzcEcUFxLM1B7MqMzBUxDMtsy2zNtVOcynaszlzIgHzOzM-RNnFcyHKMzGSsyPzLfMncyKCcznzMNmS8zVzPzMxMz_SKFl3ABLEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYMzxzOAoFszbRArM4B_MoTcXNn2hdtwBVQnMuszQTHEgzKnMggAfOjAlecynzKLMrAjMjcynR8yscMybzL09IczFdCPMsMz2zIXMhMyNCsyCT8y9DjjMsszdzO5-Wcz6zKfM4SoVVU7Mwx_MscyYzN3My8zeWT_Mz8z_EszvBczOIszvzKgBzJjMnD7MrMy1zM3Musy-zMLM3szZzNTM9T_MvQHM9T_MxczkzOfMlgXMusyczO0ECCYrMGt5Ycy9Gcy2NczEzMMCBczmzJLMk1gJCMyJzLEIzNcOzOkwCmrMmsy_R8yxFFQuNAfM28z0zOZ6zMpXVMzRzLtzK2jM8szlzJNJBl8ezJ4azNVazL59DmbM10UTLHzMuczlacz4IjVbzNQAZ8y5TGnM7yVbZczWzP_MuMzxWcz7IHPM-syoUszzNMzUzPhVzLd4Yg3M28zCBTXM9znMvsywzOLM_AHMm8z3zJHMxMzHzIUdzIxgT8zfzPQ7zMjM9zRJFMz-aszRzNVCEMy6zLsVajxczOI0DTggzK1NzPMuzJLM_mTM78ybMMynBMyKzOXM4mAiasyhOcz3ccy8zKtvzNPMiszezMBczNjM0gvM0FrMtRAcCczXAcylag3M_ifM0S7M0sylzMzM2UEJB8yEzN3MlsynzKfMnE4AKGzMuMzNzM9nD8yEBSPMnMyKzJjMu0fMnsz7zN0pzMBizIxxzK3MsqxyX2NyZWRlbnRpYWzAu3NpZ25hdHVyZV9jb3JyZWN0bmVzc19wcm9vZoKic2XcAQBHcMzKzMHM4nLMnBvMmsyRzM97zKLM_szozOdqzKJubgXM28yuzLxjJsyFzMMlfkkPa8zmzILM6gwEzJoFzOEMbllkcCkwQMyfXiRwzOXMwR8UCQ0aWszszNHMj0rM3j3MwcyVzLfM4FbMi8zlRMyKKGcpzOB4zPjMx3oezKd3IMzDzMpdIxo5zNxvzNvMgk7MlwRnH8z-Wk4pzPJuzPTM1xowzPTMrMzKzNzM7mtVzJLMrnrMtC1_zOHMuD7M_RooY8zSPSoczN1VzJbMgMyHW8zozKADGkB6zN0vITrMvirM0DoxzL1AzM4Of8z3zNzMpczEzOfMyCFfzJUTzLbMlsyiRQXM38zdY8yfzMXM18zrzO8ozNDMz8y2ecz8FhAYNsz7zPBFzOjM1GfMlcyGzLnM3cylF8yRzL3M88zuPMyqzOjMr8z4zNPMpCnMqRrM7FhjzKpazPXM2QbM2czazKB9zIxVRsyJzPMYzIbMw3d3Tk7Mm8z3zJN6zNvMlV5UAgKhY9wAIMyEzJPMosz8zJxkWSbMrznMjRY-zNLM0szxzITM5EvMlyHM2j1rCsyWzM_M4syEcFU3"
                }
            ],
            "issuanceDate": "2024-02-12T20:45:50.623123111Z"
            })

class IssuanceRequestBody(BaseModel):
    linkSecretId: str = ''
    credentialOffer: Dict = Field(alias='offer', example={
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
    credential: dict = {
        "@context": [""],
        "type": ["VerifiableCredential"],
        "issuer": {"id": settings.DID_WEB_BASE},
        "issuanceDate": '2024-02-12T20:36:33Z',
        "credentialSubject": {"sex": "male", "name": "Alex", "height": "175", "age": "28"}
    }
    credentialRequest: dict = Field(alias='request', example={
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

class IssueCredentialRequest(BaseModel):
    credential: dict = Field(example={
        "@context": [
            "https://www.w3.org/2018/credentials/v1",
            {
                '@vocab': 'urn:anoncreds:attributes#'
            }
        ],
        "type": [
            'VerifiableCredential',
            'PersonCredential'
            ],
        "issuer": settings.DID_WEB_BASE,
        "issuanceDate": '2024-02-12T20:36:33Z',
        "credentialSubject": {
            "type": ['Person'],
            "firstName": "Alice",
            "lastName": "Jones",
        }
    })
    options: dict = Field(example={
        # 'credentialSchema': {
        #     'id': ''
        # }
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