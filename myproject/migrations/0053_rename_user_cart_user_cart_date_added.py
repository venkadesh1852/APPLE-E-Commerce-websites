# Generated by Django 5.1.2 on 2024-12-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0052_remove_cart_created_at_delete_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='User',
            new_name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
