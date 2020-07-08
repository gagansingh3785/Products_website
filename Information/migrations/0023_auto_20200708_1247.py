# Generated by Django 3.0.2 on 2020-07-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0022_auto_20200618_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'other'), ('Footwear', 'Footwear'), ('Books', 'Books'), ('Clothing', 'Clothing'), ('Electronics', 'Electronics')], default='other', max_length=20),
        ),
    ]