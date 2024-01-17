from django.db import models

# Create your models here.
class Course(models.Model):
    image= models.ImageField(upload_to='admin/courses', null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    duraction = models.CharField(max_length=200, null=True, blank=True)