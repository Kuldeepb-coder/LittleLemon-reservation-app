from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

# Booking router
booking_router = DefaultRouter()
booking_router.register(r'', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/', include('restaurant.urls')),       # menu-items, message, token auth, users
    path('api/booking/', include(booking_router.urls)),  # booking API

    # Browser-friendly routes
    path('restaurant/menu/', views.MenuItemsView.as_view()),
    path('restaurant/menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('restaurant/booking/', include(booking_router.urls)),  # booking browser route
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('restaurant.urls')),
]