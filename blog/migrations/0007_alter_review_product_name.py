# Generated by Django 4.2.4 on 2023-08-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_review_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product_name',
            field=models.CharField(default='notfound', max_length=255),
        ),
    ]
