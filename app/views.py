from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import generics, serializers
from requests import Response


# class PostList(generics.ListAPIView):
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CatList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['post'] = CategorySerializer(many=True)
        return fields

    # def get(self, request):
    #     post = Post.objects.all()
    #     serializer = PostSerializer(post, many=True)
    #     return Response({'post': serializer.data})


class CatDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['post'] = CategorySerializer(many=True)
        return fields

