FROM nginx:alpine
FROM node
## Copy our default nginx config
COPY default.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# install and cache app dependencies
RUN npm install
RUN npm install -g @angular/cli
RUN npm build

## Copy over the artifacts in dist folder to default nginx public folder
COPY /dist/frontend /usr/share/nginx/html

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
