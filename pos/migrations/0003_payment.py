# Generated by Django 5.1.2 on 2024-10-24 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_remove_product_stock_product_create_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('card', 'Card'), ('bank_transfer', 'Bank Transfer')], max_length=20)),
                ('is_successful', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
