from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_e_criar_produtos, name='listar_e_criar_produtos'),
    path('produtos/<int:id>/', views.gerenciar_produto_id, name='gerenciar_produto_id'),
]