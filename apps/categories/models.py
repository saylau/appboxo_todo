from django.db import models

from .managers import CategoryManager, CategoryQueryset


class Category(models.Model):
    name = models.CharField(
        verbose_name="Category",
        max_length=255,
        blank=False
        )

    parent = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="children",
        null=True,
    )

    objects = CategoryManager.from_queryset(CategoryQueryset)()

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name
