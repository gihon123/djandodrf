from rest_framework.serializers import ModelSerializer

from apps.blog.models import BlogModel
from apps.users.models import UsersModel


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'description', 'author', 'created_at']



class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['id', 'name', 'email','username']