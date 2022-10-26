from django.core.management import BaseCommand

from reviews.models import Review
from ._load_data import _load_data


def row_saver_func(row: dict) -> None:
    obj = Review(**row)
    obj.save()


class Command(BaseCommand):
    help = f'Loads data from review.csv'

    def handle(self, *args, **options):
        _load_data(
            data_model=Review,
            data_name='review',
            row_saver_func=row_saver_func
        )
