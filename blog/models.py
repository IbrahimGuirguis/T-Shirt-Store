from django.db import models

# from django.utils import timezone

class PostProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, default='notfound')
    price = models.DecimalField(max_digits=4, decimal_places=2, default='notfound')
    image = models.ImageField(upload_to='static/image/', default='notfound')
    tshirt_color = models.ImageField(upload_to='static/image/', default='notfound')
    category = models.CharField(max_length=255, default='not found')
    date_added = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_added']


class Review(models.Model):
    # rate = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255, default='notfound')
    customer_comment = models.TextField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.CharField(max_length=255)