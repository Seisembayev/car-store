# Generated by Django 2.1.3 on 2018-11-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20181121_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=1, default=2000000, max_digits=15),
        ),
    ]
