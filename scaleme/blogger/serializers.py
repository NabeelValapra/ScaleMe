from .models import Blog
from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blogs = serializers.HyperlinkedRelatedField(many=True, view_name='blogger:blog-details', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'blogs')


class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Blog
        fields = ('id', 'owner', 'title', 'content', 'likes', 'comment')



