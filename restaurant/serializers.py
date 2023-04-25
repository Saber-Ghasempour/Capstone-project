from rest_framework.serializers import ModelSerializer
from .models import Booking, MenuItem

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'no_of_guests', 'bookingDate']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"