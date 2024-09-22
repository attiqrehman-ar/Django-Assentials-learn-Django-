from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title_Name= models.CharField(max_length=200)
    textt= models.TextField()
    description=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
