"""rpgdemesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from bot import views

router = routers.DefaultRouter()
router.register(r'personagem', views.PersonagemViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'loja', views.LojaViewSet)
router.register(r'cidade', views.CidadeViewSet)
router.register(r'jogador', views.JogadorViewSet)
router.register(r'inventario', views.ItemPersonagemViewSet)
router.register(r'estoque', views.EstoqueViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    url('remover_item/(?P<pk>[0-9]+)$', views.remover_item_inventario)
]
