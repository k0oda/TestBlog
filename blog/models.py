from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    text = models.TextField(default='')
    publication_time = models.TimeField(default=timezone.localtime(timezone.now()))
    publication_date = models.DateField(default=timezone.localdate(timezone.now()))

    def publish(self):
        self.publication_date = timezone.localdate(timezone.now())
        self.publication_time = timezone.localtime(timezone.now())
        self.save()

    def __str__(self):
        return self.title
