from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


# Handles GET (list) and POST (create)
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Handles GET (single), PUT (update), DELETE
class SingleMenuItemView(
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer