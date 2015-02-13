from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """
    We are creating this serializer class to serialize and deserialize the content to
    JSON format to sent to the different clients. This is almost similar to form API in
    django.

    When using ModelSerializer class, we only needed to give the model's name,
    the create and update statement will have default implementation.

    We have JSONParser and JSONRender to convent the object to json and vice versa.
    """
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content')




