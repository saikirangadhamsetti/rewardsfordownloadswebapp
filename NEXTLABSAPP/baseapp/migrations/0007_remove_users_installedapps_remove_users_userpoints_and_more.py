# Generated by Django 4.1.4 on 2022-12-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_activeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='InstalledApps',
        ),
        migrations.RemoveField(
            model_name='users',
            name='UserPoints',
        ),
        migrations.AlterField(
            model_name='apps',
            name='AppCategory',
            field=models.CharField(default='Entertainment', max_length=100),
        ),
        migrations.AlterField(
            model_name='apps',
            name='AppImage',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='subcategory',
            field=models.CharField(default='SocialMedia', max_length=100),
        ),
    ]
