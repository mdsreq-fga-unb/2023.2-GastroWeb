FROM node:14

WORKDIR /frontend

COPY ./frontend .

RUN npm install

EXPOSE 5147

CMD [ "npm", "run", "dev" ]
