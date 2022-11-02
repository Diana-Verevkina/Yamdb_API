import csv

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import (Category, Genre, Titles, TitlesGenre, Review, User,
                            Comment)

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


class Titles(BaseCommand):
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


class TitlesGenre(BaseCommand):
    help = 'Loading data into TitlesGenre from csv'

    def handle(self, *args, **options):
        if TitlesGenre.objects.exists():
            print('Ошибка. Данные в модель TitlesGenre уже загружены.')

        print('Загрузка данных в модель TitlesGenre')

        for row in csv.DictReader(open(f'{path}/genre_title.csv')):
            genre_title = TitlesGenre(
                id=row['id'], titles_id=row['title_id'],
                genre_id=row['genre_id']
            )
            genre_title.save()

        print('Данные в модель TitlesGenre загружены')


class User(BaseCommand):
    help = 'Loading data into User from csv'

    def handle(self, *args, **options):
        if User.objects.exists():
            print('Ошибка. Данные в модель User уже загружены.')

        print('Загрузка данных в модель User')

        for row in csv.DictReader(open(f'{path}/users.csv')):
            user = User(
                id=row['id'], username=row['username'], email=row['email'],
                role=row['role'], bio=row['bio'],
                first_name=row['first_name'], last_name=row['last_name'],
            )
            user.save()

        print('Данные в модель User загружены')


class Review(BaseCommand):
    help = 'Loading data into Review from csv'

    def handle(self, *args, **options):
        if Review.objects.exists():
            print('Ошибка. Данные в модель Review уже загружены.')

        print('Загрузка данных в модель Review')

        for row in csv.DictReader(open(f'{path}/review.csv')):
            review = Review(
                id=row['id'], title_id=row['title_id'], text=row['text'],
                author_id=row['author'], score=row['score'],
                pub_date=row['pub_date']
            )
            review.save()

        print('Данные в модель Review загружены')


class Command(BaseCommand):
    help = 'Loading data into Comment from csv'

    def handle(self, *args, **options):
        if Comment.objects.exists():
            print('Ошибка. Данные в модель Comment уже загружены.')

        print('Загрузка данных в модель Comment')

        for row in csv.DictReader(open(f'{path}/comments.csv')):
            comment = Comment(
                id=row['id'], review_id=row['review_id'], text=row['text'],
                author_id=row['author'], pub_date=row['pub_date']
            )
            comment.save()

        print('Данные в модель Comment загружены')
