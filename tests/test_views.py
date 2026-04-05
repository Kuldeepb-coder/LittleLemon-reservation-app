from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from your_app_name.models import MenuItem
from your_app_name.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Set up test client and test data
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(title="Burger", price=150, inventory=50)
        self.item2 = MenuItem.objects.create(title="Pizza", price=250, inventory=30)
    
    def test_get_all_menu_items(self):
        # Fetch all menu items via API endpoint
        response = self.client.get(reverse('menu-list'))  # 'menu-list' should match your URL name
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)