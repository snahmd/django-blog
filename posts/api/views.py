from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer
from posts.models import Post

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   
