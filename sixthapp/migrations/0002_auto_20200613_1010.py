# Generated by Django 3.0.7 on 2020-06-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixthapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
