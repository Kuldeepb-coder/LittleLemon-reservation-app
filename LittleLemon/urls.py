#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls'))
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restaurant.urls')),
    path('restaurant/menu/', include('restaurant.urls'))
]

from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/booking/', include(router.urls)),
]