from django.shortcuts import render
from django.http import HttpResponse
import string
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length', 14))
    charecter = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        charecter.extend(string.ascii_uppercase)

    if request.GET.get('Special'):
        charecter.extend(list('!@#$%^&*()_+'))

    if request.GET.get('digits'):
        charecter.extend(list('0123456789'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charecter)

    return render(request, 'generator/password.html', {'password': thepassword})
