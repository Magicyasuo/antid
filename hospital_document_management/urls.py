"""
URL configuration for hospital_document_management project.

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

from django.urls import path
from documentos import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registros/', views.lista_registros, name='lista_registros'),
    path('registros/nuevo/', views.crear_registro, name='crear_registro'),
    path('registros/<int:pk>/editar/', views.editar_registro, name='editar_registro'),
    path('registros/<int:pk>/eliminar/', views.eliminar_registro, name='eliminar_registro'),
    #negrok......................
    path('admin/', admin.site.urls),
    # Incluye las rutas de la aplicación 'documentos'
    path('registros/', include('documentos.urls')),
    # Redirige la raíz (/) a /registros/
    path('', lambda request: redirect('registros/')),
    #ngrok
    
]
