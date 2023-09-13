from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
# Create your views here.

def index(request):
    """View Function for the Index page of the site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Currently Avalibale books
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # the all() is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances': num_instances,
        'num_instances_available' : num_instances_available,
        "num_authors" : num_authors,
    }

    #Render the HTML template index.html with the data within the context variable.
    return render(request, 'index.html', context=context)