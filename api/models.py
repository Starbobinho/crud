from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
