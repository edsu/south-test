from django.db import models

# Create your models here.

class Bar(models.Model):
    requirement = models.TextField(null=False)
