# Generated by Django 4.2.4 on 2023-08-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_review_delete_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product_name',
            field=models.TextField(default='notfound', max_length=255),
        ),
    ]
