from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #First constructing a dictionary with context for the index.html to render utilizing Django template variables
    #Second return a rendered response to the client (Note 'rango/index.html' indicates the html we want to retrn
    context_dict = {'boldmessage' : 'this is pretty bold of me'}

    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page!" + "<a href='/rango/'> MainPage </a>")
