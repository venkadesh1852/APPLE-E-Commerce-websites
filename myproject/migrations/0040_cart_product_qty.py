# Generated by Django 5.1.2 on 2024-11-30 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0039_iphone_trending_iphoneplus_trending_mm_trending_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Product_qty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
