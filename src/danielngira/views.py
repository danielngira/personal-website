from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {"welcome": "hello, world!"}
    return render(request, "danielngira/index.html", context)
    

