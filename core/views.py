from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request,'home.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Usuario(
            nome = nome,
            email = email,
            senha = senha
        )
        user.save()
        #exibir novos usuários já cadastrados na página
        usuarios = {
            'usuarios': Usuario.objects.all()
            }


        return render(request, 'usuarios.html',usuarios)

