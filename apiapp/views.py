from django.shortcuts import render
from django.contrib.auth.models import User
import jwt
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apiapp.serializers import Loginserializer, UserSerializer
from rest_framework import status
from django.conf import settings





class RegisterView(GenericAPIView):
    serializer_class =  UserSerializer
    def get_queryset(self):
        return User.objects.all()
    def post(self,request):
        serializer =  UserSerializer(data = request.data)
        if   serializer.is_valid(raise_exception=True):
             serializer.save()
             return Response(serializer.data , status= status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class =Loginserializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)