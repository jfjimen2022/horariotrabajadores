from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from registro.views import FichajeViewSet, home  # <- importa también home

router = routers.DefaultRouter()
router.register(r"fichajes", FichajeViewSet)

urlpatterns = [
    path("", home, name="home"),  # <- raíz
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
