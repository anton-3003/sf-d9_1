from .models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)


class CategorySerializer(serializers.ModelSerializer):
    # posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'

    # def create(self, validated_data):
    #     authors_data = validated_data.pop('author')
    #     post = Post.objects.create(**validated_data)
    #     for a_data in authors_data:
    #         Post.objects.create(post=post, **a_data)
    #     return post

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
