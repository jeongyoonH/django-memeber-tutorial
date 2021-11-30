from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from member_management import models
# Serializer 사용


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Token
        fields = ['id', 'date', 'JWT']
