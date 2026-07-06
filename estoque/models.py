from django.db import models

class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ("Insumos", "Insumos"),
        ("Bebidas", "Bebidas"),
        ("Embalagens", "Embalagens"),
        ("Outros", "Outros")
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default="Outros")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome