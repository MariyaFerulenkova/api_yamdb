from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Comment, User, Review
from ._load_data import _load_data


def row_saver_func(row: dict) -> None:
    author_obj = get_object_or_404(User, pk=row['author'])
    review_obj = get_object_or_404(Review, pk=row['review_id'])
    obj = Comment(
        id=row['id'],
        review=review_obj,
        text=row['text'],
        author=author_obj,
        pub_date=row['pub_date']
    )
    obj.save()


class Command(BaseCommand):
    help = f'Loads data from comments.csv'

    def handle(self, *args, **options):
        _load_data(
            data_model=Comment,
            data_name='comments',
            row_saver_func=row_saver_func
        )
