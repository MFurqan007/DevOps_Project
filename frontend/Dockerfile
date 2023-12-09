FROM node:20.8.0-alpine3.18

LABEL name="Node Frontend Application" 

# Create app directory
WORKDIR /app

EXPOSE 3000

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install

COPY public/* ./public/
COPY ./.env ./
COPY app.js .

CMD [ "npm", "start" ]