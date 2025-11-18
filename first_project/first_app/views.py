from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Function Views
def MyViews(request):
    return HttpResponse('This is your views')

# Class Views
class MyViewsClass(View):
    def get(self, request):
        return HttpResponse('Hello View')