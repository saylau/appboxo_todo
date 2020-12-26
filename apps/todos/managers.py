from django.db.models import QuerySet, Manager


class TodoQueryset(QuerySet):
    def completed(self):
        return self.filter(is_completed=True)
    
    def not_completed(self):
        return self.filter(is_completed=False)
    
    def parents(self):
        return self.filter(parent=None)


class TodoManager(Manager):
    def complete_children(self, children):
        return children.update(is_complete=True)


TodoManager.from_queryset(TodoQueryset)
