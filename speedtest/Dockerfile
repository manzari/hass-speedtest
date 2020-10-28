ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY run.py /
RUN chmod a+x /run.py
CMD [ "python3", "/run.py"]
