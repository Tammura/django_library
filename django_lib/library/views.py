from rest_framework import generics
from .models import Libro
from .serializers import LibroSerializer
from django.shortcuts import render
from django.core.paginator import Paginator


class LibroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all().order_by("anno_edizione")
    serializer_class = LibroSerializer


def books_list(request):
    page_number = request.GET.get("page")
    books = Libro.objects.all().order_by("anno_edizione")
    paginator = Paginator(books, 10)
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"page_obj": page_obj})
