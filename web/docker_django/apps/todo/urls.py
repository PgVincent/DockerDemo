from django.conf.urls import url, include

from docker_django.apps.todo.views import ItemsViewSet
from . import views
from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import url, include
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page
from rest_framework import routers



router = routers.DefaultRouter(trailing_slash=False)
router.register(r'items', ItemsViewSet, base_name='ads')


urlpatterns = [
    url(r'^like$', views.like, name='like'),
    url(r'^api/', include(router.urls)),
    url(r'^$', views.home, name='home'),
]
