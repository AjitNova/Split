from django.db import models

class Users(models.Model):
    user_name   = models.CharField(max_length = 200)
    first_name  = models.CharField(max_length = 200)
    last_name   = models.CharField(max_length = 200)
    email_id    = models.EmailField(max_length=50)
    password    = models.CharField(max_length=500)