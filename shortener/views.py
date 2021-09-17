from django.shortcuts import render
import short_url
from .models import URL
from django.http import HttpResponseRedirect

# Create your views here.

def shorten(request):
    full_url = ''
    short_url = ''
    if request.method == "POST" and request.POST.get('url') != '':
        try:
            full_url = URL.objects.create(url=request.POST.get('url'))
            short_url = shortenURL(full_url.id)
            full_url.short_url = short_url
            full_url.save()
        except :
            full_url = URL.objects.get(url=request.POST.get('url'))
            short_url = full_url.short_url
    return render(request,'index.html', {
        'full_url' : full_url,
        'short_url' : short_url,
        'url' :  URL.objects.all()
    })

def redirecter(request, short):
    url = URL.objects.get(short_url = short)
    print(url)
    return HttpResponseRedirect(f'https://{url.url}')

def shortenURL(num):
    return short_url.encode_url(num)

def delete(request,short):
    url = URL.objects.get(short_url = short)
    url.delete()
    return HttpResponseRedirect('/', {'res': 'Deleted'})

def edit(request, item):
    url = URL.objects.get(short_url=item)
    if request.method == 'POST':
        update(request,item)
        return HttpResponseRedirect('/')
    return render(request,'edit.html',{
        'data' : url
    })

def update(request,short_url):
    url = request.POST.get('url')
    URL.objects.filter(short_url=short_url).update(url=url)
    