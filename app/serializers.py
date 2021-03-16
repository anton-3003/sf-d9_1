from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'
