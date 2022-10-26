from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Title, Genre, Category, TitleCategory, TitleGenre
from ._load_data import _load_data


def title_row_saver_func(row: dict) -> None:
    title_obj = Title(id=row['id'], name=row['name'], year=row['year'])
    title_obj.save()

    category_obj = get_object_or_404(Category, pk=row['category'])

    title_category_obj = TitleCategory(title=title_obj, category=category_obj)
    title_category_obj.save()


def genre_title_row_saver_func(row: dict) -> None:
    title_obj = get_object_or_404(Title, pk=row['title_id'])
    genre_obj = get_object_or_404(Genre, pk=row['genre_id'])

    title_genre_obj = TitleGenre(title=title_obj, genre=genre_obj)
    title_genre_obj.save()


class Command(BaseCommand):
    help = f'Loads data from titles.csv and genre_title.csv'

    def handle(self, *args, **options):
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
