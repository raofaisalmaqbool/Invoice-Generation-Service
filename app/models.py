from django.db import models
import datetime


# Store basic seller information
class seller(models.Model):
    name = models.CharField(max_length=50, default="Faisal")
    address = models.CharField(max_length=150, default="Lahore")
    phone = models.CharField(max_length=20, default="+0000000000")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # Display seller name in admin and shell
        return self.name


# Store buyer information for each purchase
class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    purchase_date = models.DateField(default=datetime.datetime.now)

    def __str__(self):  # Display buyer name in admin and shell
        return self.name


# Store product information used to generate invoices
class producat(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)

    def __str__(self):  # Display product name in admin and shell
        return self.name
