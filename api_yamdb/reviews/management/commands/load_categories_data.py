from django.core.management import BaseCommand

from reviews.models import Category

from ._load_data import _load_data


def row_saver_func(row: dict) -> None:
    obj = Category(**row)
    obj.save()


def _load_categories_data():
    _load_data(
        data_model=Category,
        data_name='category',
        row_saver_func=row_saver_func
    )


class Command(BaseCommand):
    help = 'Loads data from category.csv'

    def handle(self, *args, **options):
        _load_categories_data()
