"""
URL configuration for Films project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from appFilms import endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('print/JSON1', endpoint.prueba1),
    path('print/<valor1>/JSON2/<valor2>', endpoint.prueba2),
    path('print/JSON3/<valor>', endpoint.prueba3),
    path('print/JSON4/<int:valor>', endpoint.prueba4),
    path('print/JSON5', endpoint.prueba5),
    path('print/JSON6/<int:valor>', endpoint.prueba6),
    path('print/JSON7', endpoint.prueba7),
    path('films/<title>', endpoint.titulo),
]
