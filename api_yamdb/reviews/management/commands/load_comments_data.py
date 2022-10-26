from django.core.management import BaseCommand

from reviews.models import Comment
from ._load_data import _load_data


def row_saver_func(row: dict) -> None:
    obj = Comment(**row)
    obj.save()


class Command(BaseCommand):
    help = f'Loads data from comments.csv'

    def handle(self, *args, **options):
        _load_data(
            data_model=Comment,
            data_name='comments',
            row_saver_func=row_saver_func
        )
