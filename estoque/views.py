import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produto

@csrf_exempt
def listar_e_criar_produtos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all().values(
            'id', 'nome', 'descricao', 'preco', 'quantidade', 'categoria', 'data_cadastro'
        )
        return JsonResponse(list(produtos), safe=False)

    elif request.method == 'POST':
        try:
            dados = json.loads(request.body)
            novo_produto = Produto.objects.create(
                nome=dados['nome'],
                descricao=dados.get('descricao', ''),
                preco=dados['preco'],
                quantidade=dados.get('quantidade', 0),
                categoria=dados.get('categoria', 'Outros')
            )
            return JsonResponse({'mensagem': 'Produto cadastrado com sucesso!', 'id': novo_produto.id}, status=201)
        except Exception as e:
            return JsonResponse({'erro': f'Falha ao cadastrar: {str(e)}'}, status=400)

@csrf_exempt
def gerenciar_produto_id(request, id):
    try:
        produto = Produto.objects.get(id=id)
    except Produto.DoesNotExist:
        return JsonResponse({'erro': 'Produto não encontrado.'}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'id': produto.id,
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': str(produto.preco),
            'quantidade': produto.quantidade,
            'categoria': produto.categoria
        })

    elif request.method == 'PUT':
        try:
            dados = json.loads(request.body)
            produto.nome = dados.get('nome', produto.nome)
            produto.descricao = dados.get('descricao', produto.descricao)
            produto.preco = dados.get('preco', produto.preco)
            produto.quantidade = dados.get('quantidade', produto.quantidade)
            produto.categoria = dados.get('categoria', produto.categoria)
            produto.save()
            return JsonResponse({'mensagem': 'Produto atualizado com sucesso!'})
        except Exception as e:
            return JsonResponse({'erro': f'Falha ao atualizar: {str(e)}'}, status=400)

    elif request.method == 'DELETE':
        produto.delete()
        return JsonResponse({'mensagem': 'Produto excluído com sucesso!'})