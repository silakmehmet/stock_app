from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

from dj_rest_auth.serializers import TokenSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
        write_only=True, validators=[validate_password])
    password2 = serializers.CharField(
        required=True, write_only=True, validators=[validate_password])
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "password2", "token"]
        read_only_fields = ["id", "token"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({
                "detail": "Password fields didn't match!"
            })

        return data

    def create(self, validated_data):
        validated_data.pop("password2")

        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def get_token(self, obj):
        return obj.auth_token.key


class TokenUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CustomTokenSerializer(TokenSerializer):
    user = TokenUserSerializer()

    class Meta:
        model = Token
        fields = ["key", "user"]
