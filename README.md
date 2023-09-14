# fast-anoncreds
FastAPI implementation of the anoncreds-rs python wrapper


```
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload

```

## What does a did method actually do

- Access control to a registry (VDR)
- Resolve object IDs
- Ecosystems interoperability

## Server configuration

Dynamic configuration vs. pre-configuration

When it comes to did methods, revocation support and so on, should we design an api to let the client dynamically provide these options or should the server be pre configure and instead offer a discoverability of the server's configuration.

Case A:
- I want to publish a cred def, so I tell the api to publish a cred def supporting revocation with a specific did method (Indy).

Case B:
- I want to publish a cred def, so I tell the api to publish a cred def while knowing if it will support revocation and which did method it will use.

## Concerns
- Redirects are FORBIDDEN on Registry endpoints. SHOULD return 200, 404 or 500.
