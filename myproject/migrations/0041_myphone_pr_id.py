# Generated by Django 5.1.2 on 2024-12-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0040_cart_product_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='myphone',
            name='pr_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]