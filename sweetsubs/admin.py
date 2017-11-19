# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Sweetsubs
from .models import Purchase

# Register your models here.

admin.site.register(Sweetsubs)
admin.site.register(Purchase)
