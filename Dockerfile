FROM python:3.11

WORKDIR /gastroweb

ENV TZ=America/Sao_Paulo

COPY ./src/requirements.txt .

RUN pip install -r requirements.txt

COPY ./src .

EXPOSE 5000

CMD [ "python3", "main.py" ]