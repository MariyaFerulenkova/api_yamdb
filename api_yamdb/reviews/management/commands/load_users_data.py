from django.core.management import BaseCommand

from reviews.models import User
from ._load_data import _load_data


def row_saver_func(row: dict) -> None:
    obj = User(**row)
    obj.save()


class Command(BaseCommand):
    help = f'Loads data from users.csv'

    def handle(self, *args, **options):
        _load_data(
            data_model=User,
            data_name='users',
            row_saver_func=row_saver_func
        )
