from django.shortcuts import render


def home(request):
    return render(request, "base.html")


def result(request):
    return render(request, "base.html")
