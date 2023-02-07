from django.db import models

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    isPublish = models.BooleanField()
    writingDate = models.DateField()