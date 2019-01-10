# Generated by Django 2.1.3 on 2018-12-17 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_delete_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='150x150px', upload_to='images/', verbose_name='Ссылка картинки')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Car')),
            ],
        ),
    ]
