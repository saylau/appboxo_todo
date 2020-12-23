from django_filters import FilterSet

from apps.categories.models import Category


class CategoryListFilter(FilterSet):
    class Meta:
        model = Category
        fields = [
            'is_completed',
        ]
