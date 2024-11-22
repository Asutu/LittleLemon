from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
# Authentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from .models import (
	MenuItem, Booking
)
from .serializers import (
	MenuItemSerializer, BookingSerializer
)


class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer
	ordering_fields = ['title', 'price', 'featured']
	filterset_fields = ['featured']
	# 'category__title' allows to search for categories
	search_fields = ['title', 'category__title']

	def get_permissions(self):
		if(self.request.method == 'GET'):
			return [AllowAny()]
		return [IsAdminUser()]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer

	def get_permissions(self):
		if(self.request.method == 'GET'):
			return [AllowAny()]
		return [IsAdminUser()]

	def patch(self, request, *args, **kwargs):
		# Toggle 'featured', without needing a body or query.
		# To update other attributes it'd be better to create a new view
		# e.g. /menu-items/update/<pk>
		menuitem = MenuItem.objects.get(pk=self.kwargs['pk'])
		menuitem.featured = not menuitem.featured
		menuitem.save()
		return Response(
			data='Featured status of {} changed to {}'.format(
				str(menuitem.title), str(menuitem.featured))
		)


def index(request):
	return render(request, 'index.html', {})
