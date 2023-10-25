from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from apps.blog.models import BlogModel
from apps.users.models import UsersModel

from apps.api.serializers import UsersModelSerializer, BlogModelSerializer

# Create your views here.


class BlogModelViewSet(ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = UsersModel.objects.all()
    serializer_class = UsersModelSerializer