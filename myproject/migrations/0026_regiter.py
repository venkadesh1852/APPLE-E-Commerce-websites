# Generated by Django 5.1.2 on 2024-11-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0025_ggg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phonenumber', models.IntegerField(max_length=10)),
                ('WhatsApp', models.IntegerField(max_length=10)),
                ('Addresss', models.TextField(max_length=500)),
                ('Pincode', models.IntegerField(max_length=6)),
            ],
        ),
    ]
