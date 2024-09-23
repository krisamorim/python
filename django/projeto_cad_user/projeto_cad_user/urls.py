from django.urls import path
from app_cad_user import views
urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('', views.home,name='home'), #coloque aqui o que vem deposi do .com, deixe em branco para pasta raiz
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
