from django.db import models


class Products(models.Model):
    choice_category = (
        ("CLOTHES", "Clothes"),
        ("SHOES", "Shoes"),
        ("COMPUTERS", "Computers"),
        ("CARS", "Cars"),
        ("BOOKS", "Books"),
    )
    choice_size = (
        # (XS, S, M, L, XL, XXL, XXL)
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXS', 'XXS'),
    )

    choice_color = (
        ('BLACK', 'Black'),
        ('WHITE', 'White'),
        ('RED', 'Red'),
        ('BLUE', 'Blue'),
        ('GREEN', 'Green'),

    )

    title = models.CharField(max_length=15)
    price = models.SmallIntegerField()
    photos = models.ImageField(upload_to='images/')
    description = models.TextField()
    availability = models.BooleanField()
    category = models.CharField(max_length=40, choices=choice_category, default='BOOKS')
    size = models.CharField(max_length=4, choices=choice_size, default='M')
    color = models.CharField(max_length=10, choices=choice_color, default='WHITE')


    class Meta:
        db_table = 'products'

    def __str__(self):
        return f'- {self.title}'

