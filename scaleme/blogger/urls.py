from django.conf.urls import url
from blogger import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^blogs/$', views.BlogList.as_view()),
    url(r'^blogs/(?P<pk>[0-9]+)/$', views.BlogDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json',])
