from django.test import TestCase
from decimal import Decimal

from restaurant.models import MenuItem, Category
from restaurant.serializers import MenuItemSerializer


class MenuItemModelTest(TestCase):
	def setUp(self):
		self.cat_salad = Category.objects.create(title='Salads')
		self.cat_dessert = Category.objects.create(title='Deserts')
		MenuItem.objects.create(
			title='Ice Cream', price=5.99, inventory=50,
			category=self.cat_dessert)
		MenuItem.objects.create(
			title='Greek Salad', price=10.5, inventory=15,
			category=self.cat_salad)

	def test_menu_item_creation(self):
		item = MenuItem.objects.get(title='Ice Cream')
		self.assertEqual(item.price, Decimal('5.99'))
		self.assertEqual(item.inventory, 50)

	def test_string_representation(self):
		item = MenuItem.objects.get(title='Greek Salad')
		self.assertEqual(str(item), 'Greek Salad')

	def test_getall(self):
		items = MenuItem.objects.all()
		serializer = MenuItemSerializer(items, many=True)

		# Check the serialized QuerySet data
		expected_data = [
			{
				'id': items[0].id,  # IDs are auto-generated, so match dynamically
				'title': 'Ice Cream',
				'price': '5.99',
				'inventory': 50,
				'featured': False,
				'description': '',
				'category': self.cat_dessert.id,
			},
			{
				'id': items[1].id,
				'title': 'Greek Salad',
				'price': '10.50',
				'inventory': 15,
				'featured': False,
				'description': '',
				'category': self.cat_salad.id,
			}
		]

		self.assertEqual(serializer.data, expected_data)
