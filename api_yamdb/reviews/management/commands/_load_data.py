from csv import DictReader
from typing import Callable

from django.db import models

ALREADY_LOADED_ERROR_MESSAGE = '''
If you need to reload the {} data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables'''


def _load_data(
        data_model: models.Model,
        data_name: str,
        row_saver_func: Callable
) -> None:
    # Show this if the data already exist in the database
    if data_model.objects.exists():
        print(f'{data_name} data already loaded...exiting.')
        print(ALREADY_LOADED_ERROR_MESSAGE.format(data_name))
        return

    # Show this before loading the data into the database
    print(f'Loading {data_name} data')

    # Code to load the data into database
    for row in DictReader(open(f'./static/data/{data_name}.csv', encoding='utf-8')):
        row_saver_func(row)
