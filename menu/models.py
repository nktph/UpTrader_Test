from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_ancestors(self):
        ancestors = []
        parent = self.parent
        while parent:
            ancestors.append(parent)
            parent = parent.parent
        ancestors.reverse()
        return ancestors
