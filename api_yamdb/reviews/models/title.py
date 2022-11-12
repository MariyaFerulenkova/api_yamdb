from django.db import models

from . import Category, Genre
from .validators import validate_year


class Title(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=200
    )
    year = models.IntegerField(
        verbose_name='Year',
        validators=(validate_year,)
    )
    description = models.CharField(
        verbose_name='Description',
        max_length=200
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Genre',
        related_name='titles',
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Category',
        related_name='titles',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.name
