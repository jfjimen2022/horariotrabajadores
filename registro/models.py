from django.db import models


class Fichaje(models.Model):
    TIPOS = [
        ("entrada", "Entrada"),
        ("salida", "Salida"),
    ]

    trabajador_id = models.CharField(max_length=20)  # Código de trabajador
    nombre = models.CharField(max_length=100, blank=True)  # opcional
    apellidos = models.CharField(max_length=100, blank=True)  # opcional
    tipo = models.CharField(max_length=10, choices=TIPOS)
    timestamp = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()
    accuracy = models.FloatField(null=True, blank=True)
    device = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trabajador_id} - {self.tipo} ({self.timestamp})"
