# Generated by Django 5.1.1 on 2024-11-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_payment_table_order_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_id',
            field=models.CharField(max_length=50),
        ),
    ]
