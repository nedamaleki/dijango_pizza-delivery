# Generated by Django 3.0.8 on 2020-08-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0005_remove_ordermodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]