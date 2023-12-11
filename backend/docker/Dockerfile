FROM python:3.11

WORKDIR /backend

RUN apt-get update && \
    apt-get -qq -y install netcat-openbsd


ENV TZ=America/Sao_Paulo

COPY ./backend/requirements.txt .


RUN pip install -r requirements.txt

COPY ./backend .

RUN chmod +x docker/start.sh

EXPOSE $PORT

CMD ["/bin/bash", "./docker/start.sh", "--host", "0.0.0.0", "--port", "$PORT"]
