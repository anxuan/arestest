from django.db import models

# Create your models here.

class cookie1(models.Model):
  id = models.AutoField(primary_key=True)
  cookie1 = models.CharField(max_length=256,null=False,unique=True)
