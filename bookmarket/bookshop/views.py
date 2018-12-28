import itertools
import pdb

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.utils import json

from .Serializers import BookSerializer, AuthorSerializer, GenreSerializer, SubGenreSerializer
from .models import Book, Author, Genre, SubGenre
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

class BookCompleteDetailsViewSet(ObjectMultipleModelAPIViewSet):
    add_model_type = False
    querylist = (
        {
            'queryset': Book.Objects.all(),
            'serializer_class': BookSerializer,
            'label': 'Book',
        },
        {
            'queryset': Author.Objects.all(),
            'serializer_class': AuthorSerializer,
            'label': 'Authors'
        },
        {
            'queryset': Genre.Objects.all(),
            'serializer_class': GenreSerializer,
            'label': 'Genre',
        },
        {
            'queryset': SubGenre.Objects.all(),
            'serializer_class': SubGenreSerializer,
            'label': 'SubGenre'
        }
    )


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.Objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.Objects.all()
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.Objects.all()
    serializer_class = GenreSerializer

class SubGenreViewSet(viewsets.ModelViewSet):
    queryset = SubGenre.Objects.all()
    serializer_class = SubGenreSerializer


@api_view(['GET'])
def get_delete_update_product(request):
    books = Book.Objects.all()
    final = []
    #pdb.set_trace()
    for book in books:
        record=[]
        author = book.author
        subgenre = author.sub_genre
        genre = subgenre.genre

        record = list([book, author, subgenre, genre])
        qs_json = serializers.serialize('json', record, indent=4)
        final.append(qs_json)
    return HttpResponse(final, content_type='application/json')
