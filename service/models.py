from django.db import models
class service(models.Model):
    service_title=models.CharField( max_length=50)
    service_desc=models.TextField()

# Create your models here.
