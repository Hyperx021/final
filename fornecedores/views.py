import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Fornecedor

@csrf_exempt
def listar_e_criar_fornecedores(request):
    if request.method == 'GET':
        fornecedores = Fornecedor.objects.all().values('id', 'nome', 'empresa', 'telefone')
        return JsonResponse(list(fornecedores), safe=False)

    elif request.method == 'POST':
        try:
            dados = json.loads(request.body)
            novo = Fornecedor.objects.create(
                nome=dados['nome'], empresa=dados['empresa'], telefone=dados.get('telefone', '')
            )
            return JsonResponse({'mensagem': 'Fornecedor cadastrado!', 'id': novo.id}, status=201)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)

@csrf_exempt
def gerenciar_fornecedor_id(request, id):
    try:
        fornecedor = Fornecedor.objects.get(id=id)
    except Fornecedor.DoesNotExist:
        return JsonResponse({'erro': 'Não encontrado.'}, status=404)

    if request.method == 'GET':
        return JsonResponse({'id': fornecedor.id, 'nome': fornecedor.nome, 'empresa': fornecedor.empresa, 'telefone': fornecedor.telefone})

    elif request.method == 'PUT':
        dados = json.loads(request.body)
        fornecedor.nome = dados.get('nome', fornecedor.nome)
        fornecedor.empresa = dados.get('empresa', fornecedor.empresa)
        fornecedor.telefone = dados.get('telefone', fornecedor.telefone)
        fornecedor.save()
        return JsonResponse({'mensagem': 'Atualizado com sucesso!'})

    elif request.method == 'DELETE':
        fornecedor.delete()
        return JsonResponse({'mensagem': 'Excluído com sucesso!'})