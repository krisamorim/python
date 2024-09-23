from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salva os dados da tela no DB
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Exibe todos os usuários cadastrados 
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Retorna os dados para