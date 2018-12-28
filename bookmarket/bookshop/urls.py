from django.conf.urls import url
from django.urls import path, include
from rest_framework import request,routers

from .views import BookViewSet, AuthorViewSet, GenreViewSet, SubGenreViewSet, BookCompleteDetailsViewSet
from . import views

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('genres', GenreViewSet)
router.register('subgenres', SubGenreViewSet)
router.register('full_details',BookCompleteDetailsViewSet,base_name='full_details')

urlpatterns = [
    path('', include(router.urls)),
    path('complete_books_details/', views.get_delete_update_product)
]