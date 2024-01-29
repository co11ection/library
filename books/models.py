from django.db import models

from authors.models import Authors
from genre.models import Genres
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, releted_name='books')
    genre = models.ManyToManyField(Genres, related_name='books')
    create_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_place=2, validators = [
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=1000000000)
    ])