from audioop import reverse
from contextlib import _RedirectStream
from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners

from . import service

def index(request):
    return render(request, 'urlshorten/index.html')


def shorten_post(request):
    return shorten(request, request.POST['url'])

# Create your views here.
def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return render(request, 'urlshorten/link.html', {'shortened_url': shortened_url})




def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return _RedirectStream(original_url)