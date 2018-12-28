from django.db import models


class Genre(models.Model):
    '''
        Model for Genre
    '''

    name = models.CharField(max_length=20,blank=False)
    genredetails = models.TextField(blank=False)
    slug = models.CharField(max_length=20, blank=False)
    MetaData = models.TextField(blank=True)
    Objects = models.Manager()

class SubGenre(models.Model):
    '''
        Models for sub genre
    '''

    name = models.CharField(max_length=20, blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,related_name='SubGenre')
    description = models.TextField(blank=False)
    slug = models.CharField(max_length=20, blank=False)
    Objects = models.Manager()

class Author(models.Model):
    '''
        Author model with forien key "author in Book model
    '''

    author_name = models.CharField(max_length=20,blank=False)
    sub_genre = models.ForeignKey(SubGenre, on_delete=models.CASCADE, related_name='Author')
    author_rating = models.IntegerField(blank=True)
    about_author = models.TextField(blank=True)
    Objects = models.Manager()

class Book(models.Model):
    '''
        Model represent books
    '''
    name = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='Book')
    status = models.CharField(max_length=25, blank=False, default='Unpublished')
    cost = models.DecimalField(default=0.0, blank=False, max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=20,default='Ruppes', blank=False)
    publish_time = models.DateTimeField(auto_now=True)
    Objects = models.Manager()