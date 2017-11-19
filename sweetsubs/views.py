# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Sweetsubs
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def all_sweetsubs(request):
    sweetsubss = Sweetsubs.objects.all()
    return render(request, "sweetsubs/sweetsubs.html", {"sweetsubss": sweetsubss})

