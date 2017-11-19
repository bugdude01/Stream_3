# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Contact(models.Model):

    class Meta:# include this to ensure build in IDE
        app_label = "CandyLand_app"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    address_3 = models.CharField(max_length=255)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])



