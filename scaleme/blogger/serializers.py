from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.Serializer):
    """
    We are creating this serializer class to serialize and deserialize the content to
    JSON format to sent to the different clients. This is almost similar to form API in
    django.
    """
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    content = serializers.CharField(style={'base_template':'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a  new 'Blog' instance, given the validated data.
        """
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Blog' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()


