from django.template.context import RequestContext
from forms import AddressBookForm
from django.shortcuts import render_to_response, HttpResponse
import json

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
            return HttpResponse("You entry has successfully saved to our database. Thanks.!!")

    return render_to_response('sample.html', {'form':form}, RequestContext(request))


def ajax_add(request):
    form = AddressBookForm()
    response_data = {}

    if request.POST and request.is_ajax():
        form = AddressBookForm(request.POST)
        response_data['status'] = 'false'
        if form.is_valid():
            form.save()
            response_data['status'] = 'true'
        else:
            error = {}
            for e in form.errors.iteritems():
                error.update({e[0]:unicode(e[1])})
            response_data['error'] = error

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    return render_to_response('sample.html', {'form':form}, RequestContext(request))



