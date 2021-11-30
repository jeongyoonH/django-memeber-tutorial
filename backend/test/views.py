from django.contrib.auth.models import User, Group
# django 의 모델을 가져올 때는 auth.models 를 활용한다.
from rest_framework import viewsets
from rest_framework import permissions
from test import serializers
from test import models

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import Http404
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer


class TokenList(APIView):
    def get(self, request, format=None):
        tokens = models.Token.objects.all()
        serializer = serializers.TokenSerializer(tokens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.TokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Token.objects.get(id=pk)
        except models.Token.DoseNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        token = self.get_object(pk)
        serializer = serializers.TokenSerializer(token)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        token = self.get_object(pk)
        serializer = serializers.TokenSerializer(token, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        token = self.get_object(pk)
        token.delete()
        return Response(status.HTTP_204_NO_CONTENT)
