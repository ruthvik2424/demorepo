FROM docker.io/library/httpd
WORKDIR /code
COPY ./index.html /usr/local/apache2/htdocs
COPY ./app.py /code
EXPOSE 80
CMD ["httpd-foreground"]
