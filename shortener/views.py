from django.shortcuts import render, redirect
from .utils import shortenURL, update, check_valid_url
from .models import URL
from django.http import HttpResponseRedirect

# Create your views here.

def shorten(request):
    full_url = ''
    short_url = ''
    if request.method == "POST":
        user_url = check_valid_url(request.POST.get('url'))
        if not URL.objects.filter(url=user_url):
            full_url = URL.objects.create(url=user_url)
            short_url = shortenURL(full_url.id)
            full_url.short_url = short_url
            full_url.save()
        else:
            full_url = URL.objects.get(url=user_url)
            short_url = full_url.short_url
    return render(request,'index.html', {
        'full_url' : full_url,
        'short_url' : short_url,
        'url' :  URL.objects.all()
    })

def redirecter(request, short):
    url = URL.objects.get(short_url = short)
    print(url)
    return HttpResponseRedirect(url.url)

def delete(request,short):
    url = URL.objects.get(short_url = short)
    url.delete()
    return redirect('/')

def edit(request, item):
    url = URL.objects.get(short_url=item)
    if request.method == 'POST':
        update(request,item,URL)
        return redirect('/')
    return render(request,'edit.html',{
        'data' : url
    })
