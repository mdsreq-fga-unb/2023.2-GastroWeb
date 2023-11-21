FROM python:3.11

WORKDIR /gastroweb

ENV TZ=America/Sao_Paulo

COPY ./backend/requirements.txt .

RUN pip install -r requirements.txt

COPY ./backend .

EXPOSE 5000

CMD [ "python3", "main.py" ]