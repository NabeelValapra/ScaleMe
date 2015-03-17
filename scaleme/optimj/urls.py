from django.conf.urls import url, patterns
from optimj import views

urlpatterns = patterns('',
    # Caching example is set in this view
    #url(r'^add/', views.add, name='address-book'),

    url(r'ajax-add/' , views.ajax_add, name='ajax-address-book'),
)
