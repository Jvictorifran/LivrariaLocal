from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)


class AutorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AutorAdmin)
