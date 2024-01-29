from django.db import models


class Genres(models.Model):
    GENRE_CHOICES = (
        ('fantastic', 'Фантастика'),
        ('horor', 'Ужасы'),
        ('detecrive', 'Детективы'),
        ('dramma', 'Драмма')
    )
    
    slug = models.SlugField(max_length=50, primary_key=True, blank=True, unique=True)
    title = models.CharField(max_length=50, choices=GENRE_CHOICES)

