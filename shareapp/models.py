from django.db import models

class Files(models.Model):
    key = models.CharField(max_length=32,unique=True)
    file = models.FileField()


