FROM python:3.9.13-slim

WORKDIR /vc-api

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app ./app
COPY data ./data
COPY config.py main.py .env ./


CMD [ "python", "main.py" ]