from django.db import models


class Autore(models.Model):
    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"

    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} {self.cognome}"


class Editore(models.Model):
    class Meta:
        verbose_name = "Editore"
        verbose_name_plural = "Editori"

    ragione_sociale = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.ragione_sociale


class Libro(models.Model):
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"

    titolo = models.CharField(max_length=200)
    editore = models.ForeignKey(Editore, on_delete=models.PROTECT)
    anno_edizione = models.IntegerField(blank=True, null=True)
    autori = models.ManyToManyField(Autore)

    def __str__(self):
        return self.titolo
