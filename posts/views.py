import datetime

from django.shortcuts import HttpResponse,redirect

# Create your views here.
'''MVC - Model View Controller'''


def hello_view(request):
    if request.method == "GET":
        return HttpResponse("Hello its my project :)")

def get_youtube(request):
    if request.method == "GET":
        return redirect("https://www.youtube.com/")

def get_date(request):
    current_date = datetime.datetime.now().date()
    if request.method == "GET":
        return HttpResponse(f"Дата: {current_date}")

def say_goodby(request):
    if request.method == "GET":
        return HttpResponse("Goodby user!")