from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',
                            max_length=100)
    slug = models.SlugField(verbose_name='Слаг категории', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра',
                            max_length=100)
    slug = models.SlugField(verbose_name='Слаг жанра', unique=True, )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(verbose_name='Название произведения',
                            max_length=200)
    year = models.IntegerField(verbose_name='Год произведения')
    description = models.TextField(verbose_name='Описание', blank=True,
                                   null=True)
    genre = models.ForeignKey(Genre, verbose_name='Жанр',
                              on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='genre',
                              help_text='Жанр произведения')
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 on_delete=models.SET_NULL, blank=True,
                                 null=True, related_name='category',
                                 help_text='Категория произведения')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    VALUE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10')
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    name = models.ForeignKey(
        Titles, on_delete=models.CASCADE,
        related_name='reviews', blank=True, null=True)
    text = models.TextField()
    score = models.CharField(max_length=2, choices=VALUE, default=1)
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments', blank=True, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.text