from .views import PostList, PostDetail, CatList, CatDetail
from django.urls import path


app_name = 'app'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('categories/', CatList.as_view(), name='cat-list'),
    path('categories/<int:pk>', CatDetail.as_view(), name='cat-detail')
]