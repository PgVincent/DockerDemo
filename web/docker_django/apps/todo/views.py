from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from .models import Item
from redis import Redis

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from docker_django.apps.todo.serializers import ItemSerializer

redis = Redis(host='redis', port=6379)


def home(request):

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all().order_by('-id')
    counter = redis.incr('counter')
    return render(request, 'home.html', {'items': items, 'counter': counter})


def like(request):
    return home(request)


class ItemsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

