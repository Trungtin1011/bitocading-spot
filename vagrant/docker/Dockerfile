FROM ubuntu
RUN apt-get -y update 
RUN apt-get install -y apache2 
RUN apt-get clean
COPY index.html /var/www/html/
EXPOSE 80
CMD apachectl -D FOREGROUND 
