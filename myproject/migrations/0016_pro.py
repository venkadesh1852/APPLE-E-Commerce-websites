# Generated by Django 5.1.2 on 2024-11-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0015_my'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('InTheBox', models.CharField(max_length=100)),
                ('I_name', models.CharField(max_length=100)),
                ('Warranty', models.CharField(max_length=50)),
                ('W_name', models.CharField(max_length=100)),
            ],
        ),
    ]