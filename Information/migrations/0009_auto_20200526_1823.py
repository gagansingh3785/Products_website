# Generated by Django 3.0.6 on 2020-05-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0008_auto_20200526_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Footwear', 'Footwear'), ('Books', 'Books'), ('Electronics', 'Electronics'), ('other', 'other')], default='other', max_length=20),
        ),
        migrations.AlterField(
            model_name='info',
            name='type_of_user',
            field=models.CharField(choices=[('Seller', 'Seller'), ('Buyer', 'Buyer')], default=None, max_length=10),
        ),
    ]
