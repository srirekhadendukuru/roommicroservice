FROM ghcr.io/codyben/csc5991-hospital-microservices/hospital-base:main

ENV SERVICE_NAME room-microservice
WORKDIR /app

ADD main.py .
COPY dashboard/* ./dashboard/

EXPOSE 80

CMD ["python", "main.py"]