from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa
    
