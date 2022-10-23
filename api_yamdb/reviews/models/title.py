from django.db import models

from . import Category, Genre


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.IntegerField()
    description = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
