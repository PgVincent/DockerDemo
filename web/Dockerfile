FROM python:3.5-onbuild
RUN pip3 install django-grappelli
RUN pip install djangorestframework
RUN pip install markdown       # Markdown support for the browsable API.
RUN pip install django-filter  # Filtering support
RUN python manage.py collectstatic