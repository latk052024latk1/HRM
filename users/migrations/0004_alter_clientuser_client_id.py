# Generated by Django 4.1.1 on 2023-05-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_clientuser_client_id_alter_clientuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientuser',
            name='client_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
