# Generated by Django 5.1.2 on 2024-12-01 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0041_myphone_pr_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myproject.myphone'),
        ),
    ]
