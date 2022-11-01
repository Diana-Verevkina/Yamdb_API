import csv

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Category, Genre, Titles

path = f'{settings.BASE_DIR}/static/data'


class Category(BaseCommand):
    help = 'Loading data into Category from csv'

    def handle(self, *args, **options):
        if Category.objects.exists():
            print('Ошибка. Данные в модель Category уже загружены.')

        print('Загрузка данных в модель Category')

        for row in csv.DictReader(open(f'{path}/category.csv')):
            category = Category(
                id=row['id'], name=row['name'], slug=row['slug']
            )
            category.save()

        print('Данные в модель Category загружены')


class Genre(BaseCommand):
    help = 'Loading data into Genre from csv'

    def handle(self, *args, **options):
        if Genre.objects.exists():
            print('Ошибка. Данные в модель Genre уже загружены.')

        print('Загрузка данных в модель Genre')

        for row in csv.DictReader(open(f'{path}/genre.csv')):
            genre = Genre(
                id=row['id'], name=row['name'], slug=row['slug']
            )
            genre.save()

        print('Данные в модель Genre загружены')


class Command(BaseCommand):
    help = 'Loading data into Titles from csv'

    def handle(self, *args, **options):
        if Titles.objects.exists():
            print('Ошибка. Данные в модель Titles уже загружены.')

        print('Загрузка данных в модель Titles')

        for row in csv.DictReader(open(f'{path}/titles.csv')):
            titles = Titles(
                id=row['id'], name=row['name'], year=row['year'],
                category_id=row['category']
            )
            titles.save()

        print('Данные в модель Titles загружены')



