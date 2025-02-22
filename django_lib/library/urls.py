from django.urls import path
from .views import books_list, LibroListCreateAPIView

urlpatterns = [
    path("", books_list, name="home"),
    path("api/books/", LibroListCreateAPIView.as_view(), name="api_books_list"),
]
