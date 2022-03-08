FROM php:8.1-apache
RUN docker-php-ext-install mysqli pdo pdo_mysql
RUN a2enmod userdir
RUN a2enmod rewrite
ADD userdir.conf /etc/apache2/mods-enabled/
