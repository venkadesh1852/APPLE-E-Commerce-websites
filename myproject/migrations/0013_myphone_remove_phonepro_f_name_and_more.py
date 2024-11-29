# Generated by Django 5.1.2 on 2024-11-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0012_remove_features_l_name_remove_features_m_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='myphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('i_image', models.ImageField(upload_to='pic')),
                ('price', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='phonepro',
            name='F_name',
        ),
        migrations.RemoveField(
            model_name='phonepro',
            name='Features',
        ),
    ]