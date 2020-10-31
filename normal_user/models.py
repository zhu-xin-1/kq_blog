from django.db import models

# Create your models here.
class normal_user(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_authority = models.ForeignKey("Authority", on_delete=models.CASCADE,null=True, blank=True)
class Authority(models.Model):
    authority_degree = models.SmallIntegerField(null=True, blank=True)
    authorit_query=models.BooleanField(null=True, blank=True)
    authorit_add = models.BooleanField(null=True, blank=True)
    authorit_delete = models.BooleanField(null=True, blank=True)
    authorit_update = models.BooleanField(null=True, blank=True)