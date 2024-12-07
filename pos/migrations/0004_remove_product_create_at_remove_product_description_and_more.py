# Generated by Django 5.1.2 on 2024-10-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='product_list/product-default.png', null=True, upload_to='products/'),
        ),
    ]
