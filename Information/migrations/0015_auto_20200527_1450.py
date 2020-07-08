# Generated by Django 3.0.6 on 2020-05-27 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0014_auto_20200527_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='type_of_user',
            field=models.CharField(choices=[('Seller', 'Seller'), ('Buyer', 'Buyer')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Footwear', 'Footwear'), ('Clothing', 'Clothing'), ('Electronics', 'Electronics'), ('other', 'other'), ('Books', 'Books')], default='other', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Information.Info'),
        ),
    ]