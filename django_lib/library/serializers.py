from rest_framework import serializers
from .models import Autore, Editore, Libro


class AutoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autore
        fields = ["nome", "cognome"]


class EditoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editore
        fields = ["ragione_sociale", "indirizzo", "telefono"]


class LibroSerializer(serializers.ModelSerializer):
    autori = AutoreSerializer(many=True)
    editore = EditoreSerializer()

    class Meta:
        model = Libro
        fields = ["id", "titolo", "editore", "anno_edizione", "autori"]

    def create(self, validated_data):
        autori_data = validated_data.pop("autori")
        editore_data = validated_data.pop("editore")
        editore, _ = Editore.objects.get_or_create(
            ragione_sociale=editore_data["ragione_sociale"],
            defaults={
                "indirizzo": editore_data.get("indirizzo"),
                "telefono": editore_data.get("telefono"),
            },
        )
        libro = Libro.objects.create(editore=editore, **validated_data)
        for autore_data in autori_data:
            autore, _ = Autore.objects.get_or_create(
                nome=autore_data["nome"], cognome=autore_data["cognome"]
            )
            libro.autori.add(autore)
        return libro
