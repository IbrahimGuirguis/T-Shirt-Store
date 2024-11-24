from django.db import models

class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    message = models.TextField()

class ContactInfo(models.Model):
    contact_head_paragraph = models.TextField()
    contact_head = models.CharField(max_length=255)
    contact_paragraph = models.CharField(max_length=255)
    contact_map_info = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    contact_map = models.TextField(default='notfound')