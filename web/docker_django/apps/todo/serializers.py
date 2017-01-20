from rest_framework import serializers
from docker_django.apps.todo.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('text', )
