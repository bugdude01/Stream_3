# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from CandyLand_app import models

# Create your views here.



def get_base(request):
    return render(request, 'base.html')

def get_home(request):
    return render(request, 'home.html')

def get_packages(request):
    return render(request, 'packages.html')

def get_gallery(request):
    return render(request, 'gallery.html')

def get_sweetlist(request):
    return render(request, 'sweetlist.html')

def get_bookus(request):
    return render(request, 'bookus.html')

def get_members(request):
    return render(request, 'members.html')