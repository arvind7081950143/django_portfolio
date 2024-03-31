from django.db import models
class skill(models.Model):
    skill_img=models.FileField(upload_to='skill/', max_length=250,null=True,default=None)

# Create your models here.
