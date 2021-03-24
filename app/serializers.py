from .models import Post, Category
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

    # def create(self, validated_data):
    #     as_data = validated_data.pop('author')
    #     post = Post.objects.create(**validated_data)
    #     for a_data in as_data:
    #         User.objects.create(post=post, **a_data)
    #     return post
    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
