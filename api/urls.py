from django.contrib import admin
from django.urls import path, include
from rooms.views import RoomsViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('rooms', RoomsViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rooms.urls')),
]
