from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.TextField()
    publication_date = models.DateField(default=timezone.now())

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
