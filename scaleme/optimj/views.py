from django.template.context import RequestContext
from forms import AddressBookForm
from django.shortcuts import render_to_response

from django.views.decorators.cache import cache_page
from django.core.cache import cache

import logging
logger = logging.getLogger("OptimJJ")


def add(request):
    form = AddressBookForm()
    ca = cache.get('Sample', None)
    if ca == None:
    	logger.debug('Cache Missed!!')
    else:
    	logger.debug('Cache Got!!')
#    cache.set('nabeel', 'sampletext')
#    sample = cache.get('nabeel')
    if request.POST:
    	cache.set('Sample', 'hello, world!', 60)
    	logger.debug('Cache Setted!!')
        form = AddressBookForm(request.POST)
        if form.is_valid():
            form.save()
            

    return render_to_response('sample.html', {'form':form}, RequestContext(request))
