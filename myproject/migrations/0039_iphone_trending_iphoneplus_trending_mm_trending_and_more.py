# Generated by Django 5.1.2 on 2024-11-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0038_iphoneplus_iplus_plus_plus16'),
    ]

    operations = [
        migrations.AddField(
            model_name='iphone',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-Trending'),
        ),
        migrations.AddField(
            model_name='iphoneplus',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-Trending'),
        ),
        migrations.AddField(
            model_name='mm',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-Trending'),
        ),
        migrations.AddField(
            model_name='myphone',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-Trending'),
        ),
        migrations.AddField(
            model_name='ts',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-Trending'),
        ),
    ]