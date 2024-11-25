from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_registros, name='lista_registros'),  # Página principal de registros
    path('nuevo/', views.crear_registro, name='crear_registro'),
    path('<int:pk>/editar/', views.editar_registro, name='editar_registro'),
    path('<int:pk>/eliminar/', views.eliminar_registro, name='eliminar_registro'),
    # path('login/', views.login_view, name='login'),
]
