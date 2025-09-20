from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import include

router = DefaultRouter()
router.register('book_all', BookViewSet, basename = 'book_all')

url_patterns = [
    path('books/',BookList.as_view(),name = 'book-list'),
    path('',include(router.urls)),
]