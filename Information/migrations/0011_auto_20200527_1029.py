# Generated by Django 3.0.6 on 2020-05-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0010_auto_20200527_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'other'), ('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Books', 'Books'), ('Footwear', 'Footwear')], default='other', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
    ]
