# Generated by Django 4.1.1 on 2023-05-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardocs', '0002_cars_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailers',
            name='trailer_photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/trailer_photo', verbose_name='ფაილი'),
        ),
    ]