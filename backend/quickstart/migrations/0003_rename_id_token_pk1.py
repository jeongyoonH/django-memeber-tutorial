# Generated by Django 3.2.9 on 2021-11-29 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='id',
            new_name='pk1',
        ),
    ]
