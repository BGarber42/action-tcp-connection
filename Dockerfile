FROM python:alpine
WORKDIR /usr/src/app

COPY . ./
RUN pip install -r requirements.txt

CMD [ "python", "./entrypoint.py" ]
