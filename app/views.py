from django.shortcuts import render
from django.http import HttpResponse
def jampandu(request):
    return HttpResponse("<h1><marquee>hii jampandu how r u</h1></marquee>")
def rani(request):
    return HttpResponse("<h1><marquee>hii rani how r u</h1></marquee>")
# Create your views here.
