from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate_first_name(self, data):
        return User.validate_first_name(data)

    def validate_last_name(self, data):
        return User.validate_last_name(data)

    def validate_phonenumber(self, data):
        return User.validate_phonenumber(data)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phonenumber", "password"]


class UserDetailSerializer(serializers.ModelSerializer):
    def validate_first_name(self, data):
        return User.validate_first_name(data)

    def validate_last_name(self, data):
        return User.validate_last_name(data)

    def validate_phonenumber(self, data):
        return User.validate_phonenumber(data)

    password = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phonenumber", "password"]


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
