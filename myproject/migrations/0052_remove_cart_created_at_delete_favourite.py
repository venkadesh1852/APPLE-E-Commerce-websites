# Generated by Django 5.1.2 on 2024-12-06 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0051_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_at',
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]
