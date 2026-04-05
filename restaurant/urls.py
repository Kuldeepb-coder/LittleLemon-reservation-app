from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),  # home page
    path('', include(router.urls)),       # user API
    path('items', views.MenuItemView.as_view()),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view()),
]