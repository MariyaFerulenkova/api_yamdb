from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Review, Title, User

from ._load_data import _load_data


def row_saver_func(row: dict) -> None:
    author_obj = get_object_or_404(User, pk=row['author'])
    title_obj = get_object_or_404(Title, pk=row['title_id'])
    obj = Review(
        id=row['id'],
        title=title_obj,
        text=row['text'],
        author=author_obj,
        score=row['score'],
        pub_date=row['pub_date']
    )
    obj.save()


def _load_reviews_data():
    _load_data(
        data_model=Review,
        data_name='review',
        row_saver_func=row_saver_func
    )


class Command(BaseCommand):
    help = 'Loads data from review.csv'

    def handle(self, *args, **options):
        _load_reviews_data()
