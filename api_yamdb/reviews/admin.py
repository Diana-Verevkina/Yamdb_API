from django.contrib import admin

from .models import Category, Genre, Title, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


# class TitleAdmin(admin.ModelAdmin):
#     list_display = ('name', 'year', 'description', 'genre', 'category')
#     search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title)
# admin.site.register(Title, TitleAdmin)
admin.site.register(User)
