from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import MenuItem, Category


class MenuItemViewTest(TestCase):
	def setUp(self):
		self.category = Category.objects.create(title='Main')
		self.client = Client()
		self.item = MenuItem.objects.create(
			title='Pizza', price=10.50, inventory=20,
			category=self.category)

	def test_menu_item_list_view(self):
		response = self.client.get(reverse('menu-list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Pizza')
		# self.assertTemplateUsed(response, 'menu_list.html')

	def test_menu_item_detail_view(self):
		response = self.client.get(reverse('menu-detail', args=[self.item.id]))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Pizza')
