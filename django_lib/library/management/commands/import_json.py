import json
from django.core.management.base import BaseCommand
from library.models import Autore, Editore, Libro


class Command(BaseCommand):
    help = "Importa anagrafica libri da un file JSON"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="Percorso del file JSON")

    def handle(self, *args, **kwargs):
        json_file = kwargs["json_file"]
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Importa gli autori
        autori_mapping = {}
        for autore_data in data.get("autori", []):
            autore, _ = Autore.objects.get_or_create(
                id=autore_data["id"],
                defaults={
                    "nome": autore_data["nome"],
                    "cognome": autore_data["cognome"],
                },
            )
            autori_mapping[autore_data["id"]] = autore

        # Importa gli editori
        editori_mapping = {}
        for editore_data in data.get("editori", []):
            editore, _ = Editore.objects.get_or_create(
                id=editore_data["id"],
                defaults={
                    "ragione_sociale": editore_data["ragione sociale"],
                    "indirizzo": editore_data.get("indirizzo"),
                    "telefono": editore_data.get("telefono"),
                },
            )
            editori_mapping[editore_data["id"]] = editore

        # Importa i libri
        for libro_data in data.get("libri", []):
            titolo = libro_data.get("titolo")
            anno = libro_data.get("anno edizione")
            autore_id = libro_data.get("autore")
            editore_id = libro_data.get("editore")

            editore = editori_mapping.get(editore_id)
            libro = Libro.objects.create(
                titolo=titolo, editore=editore, anno_edizione=anno
            )
            # Associa l'autore al libro
            if autore_id in autori_mapping:
                libro.autori.add(autori_mapping[autore_id])

            self.stdout.write(
                self.style.SUCCESS(f'Libro "{titolo}" importato correttamente.')
            )
