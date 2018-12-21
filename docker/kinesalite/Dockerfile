FROM node:4
MAINTAINER Vinicius Souza <hi@vsouza.com>

RUN npm install -g -q kinesalite

RUN mkdir /var/kinesalite
VOLUME /var/kinesalite

EXPOSE 4567

ENTRYPOINT ["kinesalite", "--path", "/var/kinesalite"]