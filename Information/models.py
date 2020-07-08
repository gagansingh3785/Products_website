from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tags(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name


class Info(models.Model):
    category = {
        ('Seller', 'Seller'),
        ('Buyer', 'Buyer'),
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_of_user = models.CharField(max_length=10, default=None, choices=category)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    seller = models.ForeignKey(Info, default=None, on_delete=models.CASCADE)
    product_image1 = models.ImageField(null=True, blank=True, default='default.jpg')
    product_image2 = models.ImageField(null=True, blank=True, default='default.jpg')
    product_image3 = models.ImageField(null=True, blank=True, default='default.jpg')
    product_image4 = models.ImageField(null=True, blank=True, default='default.jpg')
    tags = models.ManyToManyField(Tags, blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=20, default='other', choices={('Electronics', 'Electronics')
                                                                         , ('Footwear', 'Footwear')
                                                                         , ('Clothing', 'Clothing')
                                                                         , ('Books', 'Books')
                                                                         , ('other', 'other')
                                                                         , })
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    category = {
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
    }
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    user_info = models.ForeignKey(Info, default=None, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default=None, choices=category)
    Delivery_address = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    user_info = models.ForeignKey(Info, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name



