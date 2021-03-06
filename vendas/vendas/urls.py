"""vendas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers

from cliente.api import viewsets as clientesViewSets
from produto.api import viewsets as produtosViewSets
from compra.api import viewsets as compraViewSets

route = routers.DefaultRouter()
route.register(r'cliente', clientesViewSets.ClienteViewSet, basename="Cliente")
route.register(r'produto', produtosViewSets.ProdutoViewSet, basename="Produto")
route.register(r'compra', compraViewSets.CompraViewSet, basename="Compra")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
