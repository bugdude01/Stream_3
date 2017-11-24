# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .views import get_home
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User

# Create your tests here.


"""
class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_home)

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "home.html")
        home_page_template_output = render_to_response("home.html").content
        self.assertEqual(home_page.content, home_page_template_output)

"""


class HomePageTest(TestCase):
    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()

    def test_login(self):
        login = self.client.login(username='testuser', password='letmein')
        self.assertTrue(login)

    def test_home_page_uses_home_view(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_home)

    def test_home_page_uses_home_template(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "home.html")

    def test_home_page_logged_in_content(self):
        self.client.login(username='testuser', password='letmein')
        home_page = self.client.get('/')

        home_page_template_output = render_to_response(
            "home.html", {'user': self.user}).content
        self.assertEquals(home_page.content, home_page_template_output)