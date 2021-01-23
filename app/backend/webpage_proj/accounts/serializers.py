from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class RegisterCustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        instance = self.Meta.model(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
