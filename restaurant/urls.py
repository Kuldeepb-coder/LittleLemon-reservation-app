from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# Router for users (API)
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),                 # Home page
    path('menu-items/', views.MenuItemsView.as_view()),  # Menu list/create
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),  # Single menu
    path('message/', views.msg),                         # Protected message
    path('api-token-auth/', obtain_auth_token),          # Token auth
    path('', include(router.urls)),
]