from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lista_registros, name='lista_registros'),  # Página principal de registros
    path('nuevo/', views.crear_registro, name='crear_registro'),
    path('<int:pk>/editar/', views.editar_registro, name='editar_registro'),
    path('<int:pk>/eliminar/', views.eliminar_registro, name='eliminar_registro'),
    path('cargar_subseries/', views.cargar_subseries, name='cargar_subseries'),
    path('cargar_series/', views.cargar_series, name='cargar_series'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registros/completo/', views.lista_completa_registros, name='lista_completa_registros'),




    # path('login/', views.login_view, name='login'),
]
