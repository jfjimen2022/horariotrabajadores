from django.contrib import admin
from .models import Fichaje

@admin.register(Fichaje)
class FichajeAdmin(admin.ModelAdmin):
    list_display = ("trabajador_id", "nombre", "apellidos", "tipo", "timestamp", "created_at")
    search_fields = ("trabajador_id", "nombre", "apellidos")
    list_filter = ("tipo", "timestamp", "created_at")
