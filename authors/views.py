from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Authors
from .serializers import AuthorsSeriallizer


class AuthorsViewset(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSeriallizer
    permission_classes = (AllowAny,)
