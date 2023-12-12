FROM node:18

WORKDIR /frontend

ENV TZ=America/Sao_Paulo

COPY ./frontend .

RUN npm install

RUN yarn global add @quasar/cli

EXPOSE 9000

ENV PORT 9000

CMD ["quasar", "dev", "--host", "0.0.0.0", "--port", "$PORT"]