from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def test_getall(self):
        items = MenuItemView()