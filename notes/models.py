from django.db import models


class Notes(models.Model):
    title_Name= models.CharField(max_length=200)
    textt= models.TextField()
    description=models.TextField()
    

