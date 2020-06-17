from django.shortcuts import render, redirect
import random
from .models import urlshortdb, contactus

# Create your views here.

# Your domain
domain = "localhost:8000"


def home(request):
    if request.method == 'POST':
        url_to_short = request.POST.get('longurl')
        if not '.' in url_to_short:
            context = {
                'short': 'Please enter a valid url',
                'flag': True
            }
            return render(request, 'home.html', context=context)

        if urlshortdb.objects.filter(long_url_db=url_to_short).exists():

            shorted = str(urlshortdb.objects.get(long_url_db=url_to_short).shorted_url_db)
            shorted_url = domain + '/' + shorted
            context = {
                'short': shorted_url,
                'flag': True
            }
            return render(request, 'home.html', context=context)
        else:
            try:
                obj = urlshortdb.objects.latest('id')
                id = obj.id
            except:
                id = 1
            shorted = encode(int(id)+1000000)
            while urlshortdb.objects.filter(shorted_url_db=shorted).exists():
                shorted = short(url_to_short)
            shorted_url = domain + '/' + shorted
            context = {
                'short': shorted_url,
                'flag': True
            }
            data = urlshortdb(long_url_db=url_to_short, shorted_url_db=shorted)
            data.save()
            return render(request, 'home.html', context=context)
    else:
        context = {'flag': False, }
        return render(request, 'home.html', context=context)


def encode(id):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    ret = []
    while id > 0:
        val = id % base
        ret.append(characters[val])
        id = id // base
    return "".join(ret[::-1])


def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('contacter_name')
        user_email = request.POST.get('contacter_mail')
        user_messege = request.POST.get('contacter_messege')
        data = contactus(name=user_name, email=user_email, messege=user_messege)
        data.save()
        context = {
            'flag': True
        }
        return render(request, 'contact.html', context=context)

    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')



def short(long_url):
    to_choose = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shorted_url = ''
    for i in range(0, 4):
        random_number = random.randint(0, len(to_choose)-1)
        shorted_url += to_choose[random_number]
    return shorted_url



def redirect_me(request, my_short_url):
    if urlshortdb.objects.filter(shorted_url_db=my_short_url).exists():
        originalurl = str(urlshortdb.objects.get(shorted_url_db=my_short_url).long_url_db)
    else:
        return render(request, 'home.html')
    return redirect(originalurl)
