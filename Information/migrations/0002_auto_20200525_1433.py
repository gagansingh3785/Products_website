# Generated by Django 3.0.6 on 2020-05-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='type',
        ),
        migrations.AddField(
            model_name='info',
            name='type_of_user',
            field=models.CharField(choices=[('Buyer', 'Buyer'), ('Seller', 'Seller')], default=None, max_length=10),
        ),
    ]