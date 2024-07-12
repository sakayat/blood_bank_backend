from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework import status
from .serializers import RegistrationSerializer, UserLoginSerializer


class UserRegistration(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            return Response({"message": "User registered successfully", "token": token})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({"token": token.key, "user_id": user.id})
            else:
                return Response(
                    {"error": "Invalid credentials"}, status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors)


class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return redirect("login")