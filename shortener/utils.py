import short_url

def shortenURL(num):
    return short_url.encode_url(num)

def update(request,short_url, URL):
    url = request.POST.get('url')
    URL.objects.filter(short_url=short_url).update(url=url)

def check_valid_url(url):
    if url[0:7] =='http://' or url[0:8] == 'https://':
        return url
    return f'https://{url}'