from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=200
    )
    slug = models.SlugField(
        verbose_name='Slug',
        unique=True
    )

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name
