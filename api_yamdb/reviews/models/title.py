from django.db import models

from . import Category, Genre


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.IntegerField()
    description = models.CharField(max_length=200)
    genre = models.ManyToManyField(
        Genre,
        through='TitleGenre',
        through_fields=('title', 'genre'),
        related_name='titles',
        blank=True,
    )
    category = models.ManyToManyField(
        Category,
        through='TitleCategory',
        through_fields=('title', 'category'),
        related_name='titles',
        blank=True,
    )

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class TitleCategory(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
