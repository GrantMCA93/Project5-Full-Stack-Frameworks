# Generated by Django 2.0.13 on 2019-08-17 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20190817_1657'),
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
