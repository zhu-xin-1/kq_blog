from django.db import models

# Create your models here.
class normal_user(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
