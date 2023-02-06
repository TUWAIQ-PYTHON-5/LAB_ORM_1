from django.db import models

# Create your models here.


class orm(models.Model):

    title = models.CharField(max_length=1024)
    Content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()
