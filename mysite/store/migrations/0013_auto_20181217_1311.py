# Generated by Django 2.1.3 on 2018-12-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20181217_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
