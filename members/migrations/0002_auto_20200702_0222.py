# Generated by Django 3.0.7 on 2020-07-02 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
