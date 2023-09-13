from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    """ Model that represents a genre of book"""
    name = models.CharField(max_length=200, help_text="Enter a book Genre (e.g. Thriller)")

    def __str__(self):
        """string representing the Model Object"""
        return self.name
    
class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200, help_text="Enter the book's Language")

    def __str__(self):
        """string for representing the Model object"""
        return self.name
 
class Book(models.Model):
    """Model that represents a book"""
    title = models.CharField(max_length=200, help_text="enter the Books Title")
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null = True)

    summary = models.TextField(max_length=1000, help_text="Enter a brief description")
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text="13 char ISBN num")
    genre = models.ManyToManyField(Genre, help_text="select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["title", "author"]

    def display_genre(self):
        """Creates a string for the Genre. This is required to display the Genre in the Admin Terminal."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    
    display_genre.short_description = "Genre"

    def __str__(self):
        """ String that represents the Model object"""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access the detail record for this book"""
        return reverse('book-detail', args = [str(self.id)])
    
class BookInstance(models.Model):
    """ Models that represents a specific instance of a book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text= "Unique ID for this particulat book")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS=(
        ('m', 'Maintainance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices= LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """ String that reprrsents thje Book model instance"""
        return f'{self.id} ({self.book.title})'
    
class Author(models.Model):
    """Model utalised to represent an author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null = True, blank = True)
    date_of_death = models.DateField('Died', null=True, blank = True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance"""
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        """String that represents the model object"""
        return f'{self.last_name}, {self.first_name}'
