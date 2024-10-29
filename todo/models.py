from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.todo
