from django.db import models

class SignUP(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)