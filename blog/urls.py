from django.urls import path
from . import views
#from .views import ListaPostsView
urlpatterns = [
    #path('', views.iniciar_sesion, name='login'),  # Redirect root URL to login
    path('', views.post_list, name='post_list'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    # Add more URL patterns as needed
]
