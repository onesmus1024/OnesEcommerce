from django.test import SimpleTestCase
from django.urls import resolve,reverse
from ecommerce.views import SignUp

class TestUrls(SimpleTestCase):

    def test_signup_url(self):
        url = reverse("ecommerce:signup")
        self.assertEquals(resolve(url).func.view_class,SignUp)