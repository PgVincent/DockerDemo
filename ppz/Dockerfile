FROM ubuntu:16.04
#FROM artburkart/nginx-php-fpm-phalcon:1.3.5
#MAINTAINER Arthur Burkart <artburkart@gmail.com>

# Install V8
RUN apt-get update && apt-get install -y
RUN apt-get install -y curl subversion build-essential python-dev libreadline-dev git autoconf curl \
 gcc make re2c \
 php7.0 php7.0-json php7.0-dev \
 libpcre3-dev \
 sudo
RUN apt-get autoremove -y && apt-get clean && apt-get autoclean

RUN curl -s https://packagecloud.io/install/repositories/phalcon/stable/script.deb.sh | bash
#RUN apt-get install php5-phalcon
RUN apt-get install -y php7.0-phalcon

RUN git clone --depth=1 -v https://github.com/phalcon/zephir
WORKDIR zephir
RUN ./install-json
RUN ./install -c

