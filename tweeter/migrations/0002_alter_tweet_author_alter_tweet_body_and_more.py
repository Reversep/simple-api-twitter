# Generated by Django 4.2 on 2023-04-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
