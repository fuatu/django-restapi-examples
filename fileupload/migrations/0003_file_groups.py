# Generated by Django 3.0.7 on 2020-06-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('fileupload', '0002_auto_20200619_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='groups',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]