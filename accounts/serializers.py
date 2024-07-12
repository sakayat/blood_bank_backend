from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "confirm_password",
        ]

    def save(self):
        username = self.validated_data["username"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        password2 = self.validated_data["confirm_password"]

        if password != password2:
            raise serializers.ValidationError({"error": "password does'nt match"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "email already exists"})

        account = User(username=username, email=email)
        account.set_password(password)

        account.save()
        return account

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "password"]
        
