# Generated by Django 4.1.1 on 2023-05-26 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_clientuser_client_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientUser',
        ),
    ]