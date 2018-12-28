## Requirements
- Python 3.6
- Django (2.1.14)
- Django REST Framework

## Installation
```
	pip install django
	pip install djangorestframework
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource exposed , `books`, so we will use the following URLS - `/books/` and `/books/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`products` | GET | READ | Get all products
`products/:id` | GET | READ | Get a single product

in ""/admin/" , you can manage all models 'Books, authors, genre, subgenre' etc.

You can access each model details, using below links.

  "books"       : "http://127.0.0.1:8000/books/"
  "authors"     : "http://127.0.0.1:8000/authors/"
  "genres"      : "http://127.0.0.1:8000/genres/"
  "subgenres"   : "http://127.0.0.1:8000/subgenres/"
  "full_details"      : "http://127.0.0.1:8000/full_details/"
  "complete requirement"    : "http://127.0.0.1:8000/complete_book_details/"
