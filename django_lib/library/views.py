from rest_framework import generics
from .models import Libro
from .serializers import LibroSerializer
from django.shortcuts import render


class LibroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all().prefetch_related("autori").order_by("anno_edizione")
    serializer_class = LibroSerializer


def books_list(request):
    books = Libro.objects.all().prefetch_related("autori").order_by("anno_edizione")
    return render(request, "home.html", {"books": books})
