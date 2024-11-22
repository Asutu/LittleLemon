from django.db import models
from django.utils.text import slugify


class Category(models.Model):
	slug = models.SlugField(unique=True, blank=True)
	title = models.CharField(max_length=255, db_index=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			# generate slug only if it is not provided
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title


class MenuItem(models.Model):
	title = models.CharField(max_length=255, db_index=True)
	price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
	inventory = models.IntegerField(default=0, db_index=True)
	featured = models.BooleanField(db_index=True, default=False)
	description = models.TextField(max_length=1000, default='')
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

	def __str__(self):
		return self.title


class Booking(models.Model):
	name = models.CharField(max_length=255)
	guest_number = models.IntegerField(null=False)
	reservation_date = models.DateField(null=False, db_index=True)
	reservation_slot = models.SmallIntegerField(null=False)
	comment = models.CharField(max_length=1000, default='')

	def __str__(self):
		return self.name
