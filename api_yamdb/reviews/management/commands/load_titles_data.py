from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Category, Genre, Title, TitleGenre

from ._load_data import _load_data


def title_row_saver_func(row: dict) -> None:
    category_obj = get_object_or_404(Category, pk=row['category'])

    title_obj = Title(
        id=row['id'],
        name=row['name'],
        year=row['year'],
        category=category_obj
    )
    title_obj.save()


def genre_title_row_saver_func(row: dict) -> None:
    title_obj = get_object_or_404(Title, pk=row['title_id'])
    genre_obj = get_object_or_404(Genre, pk=row['genre_id'])

    title_genre_obj = TitleGenre(title=title_obj, genre=genre_obj)
    title_genre_obj.save()


def _load_titles_data():
    _load_data(
        data_model=Title,
        data_name='titles',
        row_saver_func=title_row_saver_func
    )

    _load_data(
        data_model=TitleGenre,
        data_name='genre_title',
        row_saver_func=genre_title_row_saver_func
    )


class Command(BaseCommand):
    help = 'Loads data from titles.csv and genre_title.csv'

    def handle(self, *args, **options):
        _load_titles_data()
