# Generated by Django 4.2.4 on 2023-08-19 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactForm',
        ),
    ]