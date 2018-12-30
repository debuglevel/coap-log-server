FROM python:2.7-alpine3.8
WORKDIR /src
ADD . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python2", "coap-log-server.py"]
