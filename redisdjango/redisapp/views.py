from django.shortcuts import render
from django.conf import settings

from django.core.cache import cache
import json

# Create your views here.
from django.views.decorators.cache import cache_page
from requests import request


def write_to_cache(request):
    key = 'hahaha'
    cache.set(key,json.dumps('qweqweqwe'),settings.NEVER_REDIS_TIMEOUT)
    return render(request,'test.html')

def read_from_cache(request):
    key = 'hahaha'
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    print(data)
    return render(request,'test.html',{'show':data})

@cache_page(60)
def a(reuqest):
    print('%%%%%%%%%%%%%%%%%%%%%%%%%')
    return render(request,'test.html')








