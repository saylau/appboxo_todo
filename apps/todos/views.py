from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.pagination import LimitOffsetPagination

from .filters import TodoListFilter
from .serializers import TodoSerializer
from .models import Todo


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoListFilter
