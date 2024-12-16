from django.shortcuts import render
from django.http import HttpResponse




def About_us(request):
    return render(request, "blog/about.html")


def Contact_us(request):
    return render(request, "blog/contact.html")








