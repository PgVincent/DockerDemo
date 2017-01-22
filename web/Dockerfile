FROM python:3.5-onbuild
RUN pip3 install django-grappelli
RUN pip3 install djangorestframework
RUN pip3 install markdown       # Markdown support for the browsable API.
RUN pip3 install django-filter  # Filtering support
RUN apt-get update
RUN apt-get install -y libssl-dev nodejs npm
RUN ln -s /usr/bin/nodejs /usr/bin/node
