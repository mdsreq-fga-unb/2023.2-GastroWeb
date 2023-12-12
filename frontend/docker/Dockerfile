FROM node:18

WORKDIR /frontend

ENV TZ=America/Sao_Paulo

COPY . .

RUN npm install

RUN yarn global add @quasar/cli

ENV PORT 9000

CMD ["quasar", "dev"]