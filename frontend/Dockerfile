FROM nginx:alpine
FROM node
## Copy our default nginx config
COPY default.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# install and cache app dependencies
RUN npm install
RUN npm install -g @angular/cli
RUN ng build --prod --output-path=dist

## Copy over the artifacts in dist folder to default nginx public folder
<<<<<<< HEAD
COPY --from=builder /ng-app/dist /usr/share/nginx/html
=======
COPY /dist /usr/share/nginx/html
>>>>>>> e3d6d46f988d847dbf6b156232d647bed0898289

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
