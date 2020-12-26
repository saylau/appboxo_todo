from django_filters import FilterSet

from apps.todos.models import Todo


class TodoListFilter(FilterSet):
    class Meta:
        model = Todo
        fields = [
            'is_completed',
        ]
