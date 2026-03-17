# AQUI QUE MANIPULA O BANDO DE DADOS
from django.db import models

# Create your models here
# Cada classe vai ser uma tabela no banco


class Topic(models.Model):
    # Assunto que o usuario ta aprendendo
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Devolve uma representação em string:
        # # Devolve uma representação em string do modelo
        return self.text


class Entry(models.Model):
    # Algo especifico aprendido sobre um assunto
    # Passando parametro de uma chave estrangeira
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Classe para dizer que o plural de entry é entries
    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.text[:50]
