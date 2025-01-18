
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'password'] 
        
    def create(self, validated_data):
            password = validated_data.pop('password', None)
            user = User.objects.create(**validated_data)
            if password:
                user.set_password(password)
                user.save()
            return user
        
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation.pop('password', None)  # Remove o campo 'password'
            return representation
            