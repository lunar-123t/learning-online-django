from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

from auth.exceptions import UsernameExit
from user.models import User

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        if User.objects.filter(username=validated_data['email']).exists():
            raise UsernameExit()
        user = UserModel.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            phonenumber=validated_data['phonenumber'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("email", "password","phonenumber" )
