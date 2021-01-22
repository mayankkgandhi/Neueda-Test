FROM python:3.7.5-alpine

COPY requirement.txt /

RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
            gcc \
            musl-dev \
            python-dev \
    && apk add openssl-dev \
               libffi-dev \
    && pip install --no-cache-dir -r requirement.txt \
    && apk del .build-deps 

COPY jsons /jsons
COPY containerA_main.py /
COPY connection.py /
COPY encrypt.py /
COPY json_to_xml.py /
COPY read_json_files.py /
ENTRYPOINT ["python","containerA_main.py"]
