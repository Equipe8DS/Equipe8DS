from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bot import views

router = routers.DefaultRouter()
router.register(r'personagem', views.PersonagemViewSet)
router.register(r'loja', views.LojaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
