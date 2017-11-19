# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Newsletter
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def all_newsletter(request):
    newsletters = Newsletter.objects.all()
    return render(request, "newsletter/newsletter.html", {"newsletters": newsletters})

