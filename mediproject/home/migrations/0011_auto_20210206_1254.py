# Generated by Django 3.1.5 on 2021-02-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210206_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='dateOfUpload',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='timeOfUpload',
            field=models.TimeField(),
        ),
    ]
