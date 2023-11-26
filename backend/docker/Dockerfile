FROM python:3.11

WORKDIR /backend

RUN apt-get update && \
    apt-get -qq -y install netcat-openbsd


ENV TZ=America/Sao_Paulo

COPY ./backend/requirements.txt .


RUN pip install -r requirements.txt

COPY ./backend .

EXPOSE 5000

RUN chmod +x docker/start.sh

CMD ./docker/start.sh