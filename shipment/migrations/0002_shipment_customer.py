# Generated by Django 4.2.3 on 2023-07-12 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_user'),
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='customer.customer'),
        ),
    ]
