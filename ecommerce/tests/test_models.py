from django.test import TestCase
from ecommerce.models import UserAddress

class TestModels(TestCase):

    def setUp(self):
        self.address = UserAddress.objects.create(street_name="ontario",state="canada",city="USA",zipcode=200)


    def test_useraddress(self):
        self.assertEquals(self.address.street_name,"ontario")
