# Generated by Django 3.0.3 on 2020-02-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
