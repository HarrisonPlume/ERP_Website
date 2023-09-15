from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
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

    #Number of Visits to the Site's homepage
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books' : num_books,
        'num_instances': num_instances,
        'num_instances_available' : num_instances_available,
        "num_authors" : num_authors,
        'num_visits' : num_visits,
    }

    #Render the HTML template index.html with the data within the context variable.
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    context_object_name = "book_list"
    # template_name = "books/my_template_name.html"

    def get_queryset(self):
        return Book.objects.all()
    
    def get_context_data(self, **kwargs):
        # call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # create any data and add it to the context
        context["some_data"] = "this is additional data"
        return context
    
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    context_object_name = "author_list"

    def get_queryset(self):
        return Author.objects.all()
    
    def get_context_data(self, **kwargs):
        # call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # create any data and add it to the context
        context["some_data"] = "this is additional data"
        return context
    
class AuthorDetailView(generic.DetailView):
    model = Author