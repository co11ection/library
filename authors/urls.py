from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import AuthorsViewset

router = DefaultRouter()
router.register('', AuthorsViewset)

urlpatterns = [
    path('', include(router.urls))
]