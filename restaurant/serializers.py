from rest_framework.serializers import ModelSerializer
from .models import Booking, Menu

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'no_of_guests', 'bookingDate']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"