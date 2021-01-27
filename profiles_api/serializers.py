from rest_framework import serializers
from .models import UserProfile

class HelloSerializer(serializers.Serializer):
    """Serializers a name filed for testing our APIview"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Seralizes a user profile objects"""
    class Meta:
        model = UserProfile
        fields = ('id', 'name','email', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'style':{'input_type': 'password'}}

    
    def create(self, validated_data):
        """Create and return new user"""

        user = UserProfile.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password'])

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)