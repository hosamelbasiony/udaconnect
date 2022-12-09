# FROM node:14.8.0-alpine3.12
FROM node:16.11.1-bullseye

WORKDIR .

COPY package.json ./
COPY package-lock.json ./

# RUN npm i webpack -g
# RUN npm link webpack
RUN npm install
RUN npm install react-scripts@3.4.3 -g
RUN npm install -g create-react-app

CMD ["pwd"]
COPY . ./

EXPOSE 3000

CMD ["npm", "start"]

# ./update_container.sh v1.4.9

