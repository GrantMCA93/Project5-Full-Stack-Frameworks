# Generated by Django 2.0.13 on 2019-08-17 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20190817_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
    ]
