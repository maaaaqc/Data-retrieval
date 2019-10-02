FROM python:3.7-alpine3.7
MAINTAINER <qingchuan.ma@nuance.com>

WORKDIR /env-data-retrieval

RUN pip install poetry
RUN apk upgrade --update && \
    apk add git && \
    rm -rf /var/cache/apk/* /tmp/* /root/.cache

ADD pyproject.toml poetry.lock ./

RUN apk add --update --no-cache --virtual .build-deps \
        g++ \
        python-dev \
        libxml2 \
        libxml2-dev && \
    apk add libxslt-dev
RUN poetry config settings.virtualenvs.create false && \
    poetry install && \
    rm -r /root/.cache
RUN apk del .build-deps

ADD *.py ./
ADD *.json ./

CMD ["python", "-v", "RunAll.py"]
