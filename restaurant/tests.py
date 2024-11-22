from django.test import TestCase

from .models import MenuItem, Category
from .serializers import MenuItemSerializer


class MenuItemTest(TestCase):
	def setUp(self):
		self.cat_salad = Category.objects.create(title='Salads')
		self.cat_desert = Category.objects.create(title='Deserts')

		self.icecream = MenuItem.objects.create(
						title='IceCream', price=80, inventory=100,
						category=self.cat_desert)
		self.salad = MenuItem.objects.create(
						title='Greek Salad', price=10.5, inventory=15,
						category=self.cat_salad)

	def test_get_item(self):
		self.assertEqual(self.icecream.title, 'IceCream')
		self.assertEqual(self.icecream.price, 80)
		self.assertEqual(self.icecream.category.title, 'Deserts')

	def test_getall(self):
		items = MenuItem.objects.all()
		serializer = MenuItemSerializer(items, many=True)

		# Check the serialized QuerySet data
		expected_data = [
			{
				'id': items[0].id,  # IDs are auto-generated, so match dynamically
				'title': 'IceCream',
				'price': '80.00',
				'inventory': 100,
				'featured': False,
				'description': '',
				'category': self.cat_desert.id,
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
