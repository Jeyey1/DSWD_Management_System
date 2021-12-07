from django.db import models

from users.models import User


class Supplier(models.Model):
    
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220, verbose_name="Barangay")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'store_supplier'
        # Add verbose name
        verbose_name = 'Out of School Youth'
    

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220, verbose_name="Barangay")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'store_buyer'
        # Add verbose name
        verbose_name = 'Pregnant Women'


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220, verbose_name="Barangay")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'store_season'
        # Add verbose name
        verbose_name = 'Elder'


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.CharField(max_length=120, verbose_name="Barangay", unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'store_product'
        # Add verbose name
        verbose_name = 'PWD'


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name