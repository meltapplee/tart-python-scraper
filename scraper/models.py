from django.db import models

class Column(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=255)
    title = models.TextField()
    summary = models.TextField()
    image = models.URLField()
    date = models.TextField()