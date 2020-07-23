from django.db import models

# Create your models here.
class Job(models.Model):
    # Image
    image = models.ImageField(upload_to='iamges/')
    # Summary
    summary = models.CharField(max_length=200)