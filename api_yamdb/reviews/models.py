from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',
                            max_length=100)
    slug = models.SlugField(verbose_name='Слаг категории', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genres(models.Model):
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
    genre = models.ForeignKey(Genres, verbose_name='Жанр',
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
