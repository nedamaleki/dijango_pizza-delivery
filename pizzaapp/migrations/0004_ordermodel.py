# Generated by Django 3.0.8 on 2020-08-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_customermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('phoneno', models.CharField(max_length=20)),
                ('ordereditems', models.CharField(max_length=40)),
            ],
        ),
    ]
