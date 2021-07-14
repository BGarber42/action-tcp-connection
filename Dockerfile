FROM python:alpine
WORKDIR /usr/src/app

COPY entrypoint.py ./

CMD [ "python", "./entrypoint.py" ]
