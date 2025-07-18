from rest_framework import serializers
from .models import Booking, Listing, Review  


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Review
        fields = '__all__'