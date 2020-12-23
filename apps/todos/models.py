from django.db import models

from apps.categories.models import Category

from .managers import TodoManager, TodoQueryset


class Todo(models.Model):
    title = models.CharField(
        verbose_name="To-Do",
        max_length=255,
        blank=False
        )
    comment = models.TextField(
        verbose_name="Comment",
        blank=True,
        null=True,
        )
    due_to = models.DateTimeField(verbose_name="Due to", null=True)
    is_completed = models.BooleanField(verbose_name="Is Completed")

    parent = models.ForeignKey(
        "Todo",
        on_delete=models.CASCADE,
        related_name="children",
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="todos"
    )

    objects = TodoManager.from_queryset(TodoQueryset)()

    class Meta:
        verbose_name="TO-DO"
        verbose_name_plural="TO-DO's"

    def __str__(self):
        return self.title

    def complete(self):
        if self.children.exists():
            Todo.objects.complete_children(self)
        self.is_completed = True
        self.save()
        return self.is_completed
