# Generated by Django 4.2.4 on 2023-08-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostProduct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='notfound', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default='notfound', max_digits=4)),
                ('image', models.ImageField(default='notfound', upload_to='static/image/')),
                ('tshirt_color', models.ImageField(default='notfound', upload_to='static/image/')),
                ('category', models.CharField(default='not found', max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('in_stock', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
