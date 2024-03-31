from django.db import models
class projects(models.Model):
    project_name=models.CharField(max_length=50)
    project_link=models.CharField(max_length=100)

# Create your models here.
