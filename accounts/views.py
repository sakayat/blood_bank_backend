from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework import status
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, UserLoginSerializer
import os
from dotenv import load_dotenv
load_dotenv()

class UserRegistration(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://blood-bank-backend-1sf7.onrender.com/api/accounts/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string(
                "confirm_mail.html", {"confirm_link": confirm_link}
            )
            email = EmailMultiAlternatives(email_subject, "", to={user.email})
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response({"message": "check your mail for active account"}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(f"https://humane-donor.netlify.app/login")


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
    def post(self, request):
        logout(request)
        return Response(
            {"message": "Successfully logged out."}, status=status.HTTP_200_OK
        )
