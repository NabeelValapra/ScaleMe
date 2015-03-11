from django.template.context import RequestContext
from forms import AddressBookForm
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import logging
logger = logging.getLogger("OptimJJ")


def add(request):
    logger.error('ErrRan an add request...')
    form = AddressBookForm()
#    cache.set('nabeel', 'sampletext')
#    sample = cache.get('nabeel')
    if request.POST:
        logger.error('Insitde an add request...')
        form = AddressBookForm(request.POST)
        if form.is_valid():
            form.save()

    return render_to_response('sample.html', {'form':form}, RequestContext(request))
