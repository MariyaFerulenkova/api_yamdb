from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=200
    )
    slug = models.SlugField(
        verbose_name='Slug',
        unique=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
