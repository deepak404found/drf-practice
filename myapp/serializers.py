from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','last_login', 'date_joined', 'first_name', 'last_name']
        read_only_fields = ['last_login', 'date_joined']
    
    def validate_email(self, value):
        """Ensure email is unique"""
        if User.objects.exclude(id=self.instance.id).filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value
    
    def update(self, instance, validated_data):
        allowed_fields = ['username', 'email', 'first_name', 'last_name']
        updated_data = {key: value for key, value in validated_data.items() if key in allowed_fields}
        print(updated_data)
        return super().update(instance, updated_data)
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
