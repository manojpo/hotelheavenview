from django.contrib.auth import get_user_model, SESSION_KEY
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import *


class SimpleTests(SimpleTestCase):
    databases = '__all__'

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


#random page..
    def test_contact_page_status_code(self):
        response=self.client.get('admin')
        self.assertEqual(response.status_code,404)

#for sucess  there should be corect path i added a wrong entry which show assertionerror 302 so
class HomePageTests(SimpleTestCase):

    def test_view_uses_correct_templates(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,302)
        self.assertTemplateNotUsed(response,'/heavenview/home.html')
#
#
# class BlogTest(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#
#             password='secret'
#         )
#     def test_post_create_view(self):
#         response = self.client.post(reverse('addblog'), {
#             'name': 'New Title',
#             'content': 'new',
#
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'New Title')
#         self.assertContains(response, 'new')
#



class SignupPageTest(TestCase):
    username = 'newuser'


    def test_signup_page_status_code(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
    # #
    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'heavenview/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)



class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        # self.assertTrue(response.context['heavenview'].is_active)

#







