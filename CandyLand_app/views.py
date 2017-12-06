# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.forms import EnquiryForm
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
import datetime
from django.core.mail import send_mail, get_connection
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


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

def get_members(request):
    return render(request, 'members.html')

def enquiry(request):
    form_class = EnquiryForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            email = request.POST.get('email', '')
            home_phone = request.POST.get('email', '')
            mobile_phone = request.POST.get('home_phone', '')
            date = request.POST.get('date', '')
            event_type = request.POST.get('event_type', '')
            number_of_guests = request.POST.get('number_of_guests', '')

            template = get_template('enquiry_template.html')

            content = template.render({
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'home_phone': home_phone,
                'mobile_phone': mobile_phone,
                'date': date,
                'event_type': event_type,
                'number_of_guests': number_of_guests,
            })

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmaol.com'],
                headers= {'reply-To': email}
            )
            email.send()
            return redirect('/thanks')

    return render(request, 'bookus.html', {
        'form': form_class,
    })

def thanks(request):
    return render(request, 'thanks.html')