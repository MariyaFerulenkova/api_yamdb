from django.core.management import BaseCommand

from .load_categories_data import _load_categories_data
from .load_comments_data import _load_comments_data
from .load_genres_data import _load_genres_data
from .load_reviews_data import _load_reviews_data
from .load_titles_data import _load_titles_data
from .load_users_data import _load_users_data


class Command(BaseCommand):
    help = f'Loads all data from csv files in static/data'

    def handle(self, *args, **options):
        _load_categories_data()
        _load_genres_data()
        _load_titles_data()
        _load_users_data()
        _load_reviews_data()
        _load_comments_data()
