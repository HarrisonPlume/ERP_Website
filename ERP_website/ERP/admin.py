from django.contrib import admin
from .models import Book, Genre, Language, Author, BookInstance

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book

#Define the Author admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth','date_of_death')

    fields = ['first_name','last_name',('date_of_birth','date_of_death')]

    inlines =[BookInline]

#Register the Author admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

#Register the admin classes for Book using the decerator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')

    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back','id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Book Details', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
