from django.db.models import QuerySet, Manager


class CategoryQueryset(QuerySet):
    def parents(self):
        return self.filter(parent=None)


class CategoryManager(Manager):
    pass


CategoryManager.from_queryset(CategoryQueryset)
