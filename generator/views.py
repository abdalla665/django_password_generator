from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html',)


def password(request):
    characters = list('abcdefgkhmnloqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHJKLMNOQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('@*&#@'))


    length = int(request.GET.get('length',12)) #12 here is a deafult value (in case the user didn't choose a number)
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})
