from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, SubGenre
@admin.register(SubGenre)
class SubGenreAdmin(admin.ModelAdmin):
    pass
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


