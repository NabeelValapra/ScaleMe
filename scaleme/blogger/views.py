from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Blog
from django.views.decorators.csrf import csrf_exempt
from .serializers import BlogSerializer

# Create your views here.
class JSONResoponse(HttpResponse):
    """
    We are inheritting the property of a HttpResponse object to behave as a JSONResoponse.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResoponse, self).__init__(content, **kwargs)


@csrf_exempt
def blog_list(request):
    """
    This function is to list all blogs and create new blogs,
    NOTE: This function is not used for updating blogs.
    """
    if request.method == "GET":
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return JSONResoponse(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parser(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResoponse(serializer.data, status=201)
        return JSONResoponse(serializer.errors, status=400)


@csrf_exempt
def blog_details(request, pk):
    """
    This function is to Retrive, Update or Delete, the Blog
    """
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return JSONResoponse(serializer)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BlogSerializer(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResoponse(serializer)
        return JSONResoponse(serializer.errors, status=404)

    elif request.method == "DELETE":
        blog.delete()
        return HttpResponse(status=400)
