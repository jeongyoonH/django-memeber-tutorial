from django.contrib.auth.models import User, Group
# django 의 모델을 가져올 때는 auth.models 를 활용한다.
from rest_framework import viewsets
from rest_framework import permissions
from member_management.serializers import UserSerializer, GroupSerializer, TokenSerializer
from member_management import models

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import Http404
from rest_framework import status
import django

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class member_management(viewsets.ModelViewSet):
    """

    """
    def sign_up(self, request):
        if request.info["method"] == "POST":
            if request.POST['password1'] == request.POST['password2']:
                try:
                    print("test")
                    user: django.contrib.auth.models.User = User.objects.create_user(
                        username=request.POST['username'],
                        password=request.POST['password1'],
                        email=request.POST['email'],
                    )
                    print(django.contrib.auth.models)
                    if isinstance(user, django.contrib.auth.models.User) and user.is_active:
                        return "회원가입 완료되었습니다. go home.html"
                    else:
                        return "회원가입이 실패하였습니다"

                except Exception as ex:
                    return f"회원가입이 실패하였습니다 {ex}"

            return "다시 회원가입 하는 페이지 sign-up.html"
        return "다시 회원가입 하는 페이지 sign-up.html"

    def login(self, request):
        from django.contrib import auth
        from django.contrib.auth import authenticate
        from django.contrib.auth.models import User
        """
        문제 :
        1. 세션 키를 발급해줘야 한다.
        2. 결국 request 객체를 사용해야한다.
        2.
        """
        from django.contrib.sessions.backends.base import SessionBase
        print("=======================")
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            # 확인하는 로직을 여기서 돌려준다.
            user: django.contrib.auth.models.User = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return "login success"
            else:
                return "login fail"

    # print("Request DEBUG")
    # print(type(Request))
    # print(Request)
    # print("Request DEBUG END")
    # print(django.contrib.auth.models.User.objects.create_user(username="dw", email=None, password="dw"))
    # print(django.contrib.auth.models.User.objects.all())


class TokenList(APIView):
    def get(self, request, format = None):
        tokens = models.Token.objects.all()
        serializer = TokenSerializer(tokens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenDetail(APIView):
    def get_object(self, request, format=None):
        try:
            models.Token.objects.all()
        except models.Token.DoseNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        token = self.get_object(pk)
        serializer = TokenSerializer(token)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        token = self.get_object(pk)
        serializer = TokenSerializer(token, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        token = self.get_object(pk)
        token.delete()
        return Response(status.HTTP_204_NO_CONTENT)
