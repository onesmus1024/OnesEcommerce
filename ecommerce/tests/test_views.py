from django.test import TestCase,Client
from ecommerce.views import AddProductView
from django.urls import reverse

class TestView(TestCase):

    def setUp(self):

        self.client = Client()
        self.addproduct_url=reverse("ecommerce:signup")

    def test_home_view(self):
        response=self.client.get(self.addproduct_url)

        self.assertEquals(response.status_code,200)
        
