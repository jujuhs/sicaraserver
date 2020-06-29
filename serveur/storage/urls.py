from django.urls import include,path
from . import views
from rest_framework import routers
from .views import PhotoViewSet

router = routers.DefaultRouter()
router.register('photos', PhotoViewSet)
urlpatterns = [
    path('accueil', views.home),
    path('',include(router.urls))
]