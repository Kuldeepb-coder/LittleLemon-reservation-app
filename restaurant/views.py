from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer

# ---- Home page ----
def index(request):
    return render(request, 'index.html', {})

# ---- Menu endpoints ----
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# ---- Booking endpoint ----
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# ---- User endpoint ----
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ---- Protected message ----
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})