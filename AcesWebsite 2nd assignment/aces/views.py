from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import applicants,Slot


def index(request):
    h=Slot




    return render(request,'aces/login.html',{'h':h})



