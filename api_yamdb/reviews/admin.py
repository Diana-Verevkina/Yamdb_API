from django.contrib import admin
from .models import Category, Genre, Titles, User

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Titles)
admin.site.register(User)
