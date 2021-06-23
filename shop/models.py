from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=15)
    category = models.ForeignKey('shop.ProductCategory', on_delete=models.CASCADE, related_name='sub_categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey('shop.ProductCategory', on_delete=models.CASCADE, related_name='products', null=True)
    subcategory = models.ForeignKey('shop.SubCategory', on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    mobile = models.IntegerField(default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to="shop/images", default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='carts')
    counter = models.IntegerField(default=1)
