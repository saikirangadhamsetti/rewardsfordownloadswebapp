# Generated by Django 4.1.4 on 2022-12-25 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_transactions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='Appid',
            new_name='AppId',
        ),
    ]
