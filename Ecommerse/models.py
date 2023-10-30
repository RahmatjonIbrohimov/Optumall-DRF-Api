from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.first_name

class Profile(models.Model):
    PHONE_CHOICES = (
        ('customer', 'Customer'),
        ('deliverer', 'Deliverer'),
    )

    phone_number = models.BigIntegerField(null=True)
    who = models.CharField(max_length=10, choices=PHONE_CHOICES)
    telegram_username = models.CharField(max_length=30, null=True)


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.image.name


class Product(models.Model):
    SIZE_CHOICES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large')
    )
    CATEGORY_CHOICES = (
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        ('category3', 'Category 3')
    )

    title = models.CharField(max_length=120)
    price = models.CharField(max_length=20)
    photos = models.ManyToManyField(Photo)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)

    def __str__(self):
        return self.title
