from django.conf.urls import url, patterns
from optimj import views

urlpatterns = patterns('',
    url(r'^add/', views.add, name='blogger'),
)
