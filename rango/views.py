from django.shortcuts import render

from django.http import HttpResponse 

def index(request):
    #construct a dictionary to pass to the template engine as its context
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #return a rendered response to send to the client 
    #make use of the shortcut function
    #the first parameter is the template we wish to use 
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Eleanor Green.'}

    return render(request, 'rango/about.html', context=context_dict)

    #return HttpResponse("Rango says here is the about page! <a href='/rango/'>Index</a>")
