from django.shortcuts import render


def index(request):
    # Pagina principal que vai ser mostrada
    return render(request, "learning_logs/index.html")
    # O return vai ser responsavel por retornar a pagina web para o usuario
