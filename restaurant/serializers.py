from django.contrib.auth.models import User
from rest_framework import serializers
from decimal import Decimal

from .models import Category, MenuItem, Booking


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'slug', 'title']
		read_only_fields = ['id']


class MenuItemSerializer(serializers.ModelSerializer):
	'''
	A MenuItem is related to a single Category by its primary key.
	'''
	# use category id field
	category = serializers.PrimaryKeyRelatedField(
		queryset=Category.objects.all(),
		required=False,
		# default=Category.objects.get(id=1)  # change default behaviour from model
	)
	# display the category string representation only (read-only)
	# category = serializers.StringRelatedField()
	# display as a nested entry
	# category = CategorySerializer(read_only=True)
	# category_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = MenuItem
		fields = '__all__'
		read_only_fields = ['id']
		extra_kwargs = {
			'price': {'min_value': Decimal(0.01)},
		}


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'
		read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
	day_joined = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = '__all__'
		read_only_fields = ['id']
		exclude = ['password', 'user_permissions', 'date_joined']

	def get_day_joined(self, obj):
		return obj.date_joined.strftime('%Y-%m-%d')
