from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.pagination import LimitOffsetPagination

from .filters import CategoryListFilter
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryListFilter
