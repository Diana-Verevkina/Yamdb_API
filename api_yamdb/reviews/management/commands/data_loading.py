import csv

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import (Category, Genre, Title, TitlesGenre, Review, User,
                            Comment)

path = f'{settings.BASE_DIR}/static/data'


class Command(BaseCommand):
    help = 'Loading all data from csv'

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

        if Genre.objects.exists():
            print('Ошибка. Данные в модель Genre уже загружены.')

        print('Загрузка данных в модель Genre')

        for row in csv.DictReader(open(f'{path}/genre.csv')):
            genre = Genre(
                id=row['id'], name=row['name'], slug=row['slug']
            )
            genre.save()

        print('Данные в модель Genre загружены')

        if Title.objects.exists():
            print('Ошибка. Данные в модель Title уже загружены.')

        print('Загрузка данных в модель Title')

        for row in csv.DictReader(open(f'{path}/titles.csv')):
            titles = Title(
                id=row['id'], name=row['name'], year=row['year'],
                category_id=row['category']
            )
            titles.save()

        print('Данные в модель Title загружены')

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



