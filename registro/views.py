from rest_framework import viewsets
from .models import Fichaje
from .serializers import FichajeSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import HttpResponse  # <- necesario para home

# Desactivar CSRF solo para desarrollo
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Ignora CSRF

class FichajeViewSet(viewsets.ModelViewSet):
    queryset = Fichaje.objects.all().order_by("-timestamp")
    serializer_class = FichajeSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

    # Método create para debug de datos recibidos
    def create(self, request, *args, **kwargs):
        print("Datos recibidos del cliente:", request.data)  # <-- imprime en consola
        return super().create(request, *args, **kwargs)

# Función home para la raíz
def home(request):
    return HttpResponse("Servidor Django activo. API disponible en /api/fichajes/")
