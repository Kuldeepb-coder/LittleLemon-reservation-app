from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'