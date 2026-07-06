from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_e_criar_fornecedores),
    path('<int:id>/', views.gerenciar_fornecedor_id),
]