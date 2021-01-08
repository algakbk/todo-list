from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Hello world!")

def test(request):
    return render(request, "test.html")

def index(request):
    return render(request, "index.html")