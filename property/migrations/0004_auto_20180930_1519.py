# Generated by Django 2.1 on 2018-09-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20180930_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='booked_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='guest',
            name='start_date',
            field=models.CharField(max_length=20),
        ),
    ]
