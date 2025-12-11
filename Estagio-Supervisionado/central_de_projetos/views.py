
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Colaborador, Gerencia, Projeto, Equipe, Tarefas, Eixo, Prioridade, Objetivo, Status, Equipe_Tarefa, Cargo,Documento
from .forms import CadColaborador, CadProjeto, CadEquipe, CadTarefa, CadEquipeTarefa
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, logout ,login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

def login(request):
    if request.user.is_authenticated:
        return redirect('home_page') 
    
    print("Método da requisição:", request.method)  # Verifica o método da requisição
    
    if request.method == 'POST':
        email = request.POST.get('username')  
        password = request.POST.get('password')
        
        print("Email:", email)  # Verifica se o email está sendo capturado
        print("Password:", password)  # Verifica se a senha está sendo capturada
        
        user = authenticate(request, email=email, password=password)

        print(user)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Usuário {user.email} logado com sucesso.')
            return redirect('home_page')
        else:
            messages.error(request, "Credenciais inválidas. Tente novamente.")
    
    print("Chegou ao final da view, não foi um POST.")
    return render(request, 'index.html')  

@never_cache
def sair(request):
    logout(request)
    return redirect('login') 


@login_required
def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'home_page.html', {'user': request.user})
    else:
        return redirect('index')  
    

def criar_projetos(request):
    form = CadProjeto()
    contexto = {
        'form':form
    }
    return render(request, 'criar_projetos.html', contexto)

@login_required
def cadastro_colaborador(request):
    form = CadColaborador()
    contexto = {
        'form':form
    }

    return render(request, 'cadastro_colaborador.html', contexto)

def cadastro_equipe(request):
    form = CadEquipe() 
    contexto = {
        'form':form
    }

    return render(request, 'cadastro_equipe.html', contexto)

def cadastro_equipe_tarefa(request):
    form  = CadEquipeTarefa()
    projetos = Projeto.objects.all()
    equipes = Equipe.objects.select_related('id_projeto', 'id_colaborador').all()
    tarefas = Tarefas.objects.select_related('id_projeto').all()

    colaboradores_por_projeto = {}
    for equipe in equipes:
        projeto_id = equipe.id_projeto.id_projeto
        if projeto_id not in colaboradores_por_projeto:
            colaboradores_por_projeto[projeto_id] = []
        colaboradores_por_projeto[projeto_id].append(equipe.id_colaborador)
    
    tarefas_por_projeto = {}
    for tarefa in tarefas:
        projeto_id_tarefa = tarefa.id_projeto.id_projeto
        if projeto_id_tarefa not in tarefas_por_projeto:
            tarefas_por_projeto[projeto_id_tarefa] = []
        tarefas_por_projeto[projeto_id_tarefa].append({
            'id_tarefa': tarefa.id_tarefa,
            'nome_tarefa': tarefa.nome_tarefa
        })

    contexto = {
        'form': form,
        'projetos': projetos,
        'colaboradores_por_projeto': colaboradores_por_projeto,
        'tarefas_por_projeto': tarefas_por_projeto,
    }
    return render(request, 'cadastro_equipe_tarefa.html', contexto)


def ver_projetos(request):
    try:
        status_concluido = Status.objects.get(nome_status="CONCLUIDO")
    except ObjectDoesNotExist:
        status_concluido = None  
        # Opcional: adicionar um log aqui
        print("Status 'CONCLUIDO' não encontrado.")

    query = request.GET.get('q', '')
    
    # Adiciona anotações para contagem total e concluída de tarefas
    if status_concluido:
        projetos = Projeto.objects.annotate(
            total_tasks=Count('tarefas'),
            tasks_feitas=Count('tarefas', filter=Q(tarefas__id_status=status_concluido.id_status))
        )
    else:
        projetos = Projeto.objects.annotate(
            total_tasks=Count('tarefas'),
            tasks_feitas=Count('tarefas', filter=Q(tarefas__id_status=None))  # Se não houver status, conta 0 tarefas feitas
        )

    if query:
        projetos = projetos.filter(
            Q(nome_projeto__icontains=query) | Q(processo_sei__icontains=query)
        )

    return render(request, 'ver_projetos.html', {'projetos': projetos})

def cadastro_tarefa(request):
    form = CadTarefa()
    projetos = Projeto.objects.all()
    equipes = Equipe.objects.select_related('id_projeto', 'id_colaborador').all()
    
    colaboradores_por_projeto = {}
    for equipe in equipes:
        projeto_id = equipe.id_projeto.id_projeto
        if projeto_id not in colaboradores_por_projeto:
            colaboradores_por_projeto[projeto_id] = []
        colaboradores_por_projeto[projeto_id].append(equipe.id_colaborador)
    contexto = {
        'form':form,
        'projetos': projetos,
        'colaboradores_por_projeto': colaboradores_por_projeto,
    }
    return render(request, 'cadastro_tarefas.html', contexto)


def projeto(request):
    if request.method == 'POST':
        form = CadProjeto(request.POST, request.FILES) 
        id_eixo = request.POST.get('id_eixo')
        eixo = get_object_or_404(Eixo, pk=id_eixo)

        id_objetivo = request.POST.get('id_objetivo')
        objetivo = get_object_or_404(Objetivo, pk=id_objetivo) 
        if form.is_valid():
            
            novo_projeto = Projeto(
                nome_projeto=form.cleaned_data['nome_projeto'],
                data_inicio=form.cleaned_data['data_inicio'],
                data_fim=form.cleaned_data['data_fim'],
                processo_sei=form.cleaned_data['processo_sei'],
                observacoes=form.cleaned_data['observacoes'],
                id_objetivo = objetivo,
                id_eixo = eixo
            )
            novo_projeto.save()

            documentos = request.FILES.getlist('documentos')  
            for arquivo in documentos:
                Documento.objects.create(
                    title=arquivo.name,
                    upload=arquivo,
                    id_projeto=novo_projeto
                )

            messages.success(request, 'Projeto e documentos cadastrados com sucesso!')
            return redirect('/criar_projetos/')
        else:
            messages.error(request, 'Erro ao cadastrar o projeto.')
    else:
        form = CadProjeto()

    return render(request, 'criar_projetos.html', {'form': form})

def colaborador(request):
    if request.method == 'POST':
        # Coletando os dados do formulário
        nome = request.POST.get('nome')
        especialidade = request.POST.get('especialidade')
        email = request.POST.get('email')
        password = request.POST.get('senha')  # Renomeado para 'password'
        valor_cargo = request.POST.get('id_cargo')
        valor_gerencia = request.POST.get('id_gerencia')

        # Verificando se todos os campos obrigatórios foram preenchidos
        if not nome or not email or not password:
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
            return redirect('/cad_colaborador/')

        # Verificando se o email já está cadastrado
        if Colaborador.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está cadastrado.')
            return redirect('/cad_colaborador/')

        # Criando o colaborador usando o manager
        cargo = get_object_or_404(Cargo, id_cargo=valor_cargo)
        gerencia = get_object_or_404(Gerencia, id_gerencia=valor_gerencia)

        novo_colaborador = Colaborador(
            nome=nome,
            especialidade=especialidade,
            email=email,
            id_cargo=cargo,
            id_gerencia=gerencia
        )
        novo_colaborador.set_password(password)  # Armazena a senha de forma segura
        novo_colaborador.save()

        messages.success(request, 'Colaborador cadastrado com sucesso!')
        return redirect('/cad_colaborador/')

    return render(request, 'cadastro_colaborador.html')  # Adicionando suporte para GET

def equipe(request):
    if request.method == 'POST':
        valor_projeto = request.POST.get('id_projeto')
        projeto = get_object_or_404(Projeto, id_projeto=valor_projeto)
        
        colaboradores_ids = request.POST.getlist('id_colaborador[]')
        
        for colaborador_id in colaboradores_ids:
            colaborador = get_object_or_404(Colaborador, id_colaborador=colaborador_id)
            
            # Verificar se a combinação já existe
            if Equipe.objects.filter(id_projeto=projeto, id_colaborador=colaborador).exists():
                messages.warning(
                    request,
                    f'O colaborador {colaborador.nome} já está associado a este projeto.'
                )
            else:
                # Criar nova equipe se a combinação não existir
                nova_equipe = Equipe(id_projeto=projeto, id_colaborador=colaborador)
                nova_equipe.save()
        
        messages.success(request, 'Colaboradores cadastrados com sucesso na equipe!')
        return redirect('/cad_equipe/')
    
    # Filtro de colaboradores não relacionados ao projeto
    if request.GET.get('id_projeto'):
        projeto_id = request.GET.get('id_projeto')
        projeto = get_object_or_404(Projeto, id_projeto=projeto_id)
        
        # Filtrar colaboradores que não estão relacionados a esse projeto em nenhuma equipe
        colaboradores_disponiveis = Colaborador.objects.exclude(
            equipe__id_projeto=projeto
        )

        # Retornar dados em formato JSON
        colaboradores_data = [
            {"id": colaborador.id_colaborador, "nome": colaborador.nome}
            for colaborador in colaboradores_disponiveis
        ]
        return JsonResponse(colaboradores_data, safe=False)
    
    form = CadEquipe()
    return render(request, 'cadastro_equipe.html', {'form': form})

def tarefa(request):
    if request.method == 'POST':
        
        id_prioridade = request.POST.get('id_prioridade')
        prioridade = get_object_or_404(Prioridade, pk=id_prioridade)

        id_status = request.POST.get('id_status')
        status = get_object_or_404(Status, pk=id_status)

        id_projeto = request.POST.get('id_projeto')
        projeto = get_object_or_404(Projeto, pk=id_projeto)

        form = CadTarefa(request.POST)
        if form.is_valid():
            
            nova_tarefa = Tarefas(
                nome_tarefa=form.cleaned_data['nome_tarefa'],
                data_inicio=form.cleaned_data['data_inicio'],
                data_fim=form.cleaned_data['data_fim'],
                observacoes=form.cleaned_data['observacoes'],
                id_prioridade = prioridade,
                id_status = status,
                id_projeto = projeto

            )

            nova_tarefa.save()
            messages.success(request, 'Tarefa cadastrado com sucesso!')
            return redirect('/cad_tarefa')
    else:
        form = CadTarefa()
    return render(request, 'cadastro_tarefas.html', {'form':form})

def equipetarefa(request):
    if request.method == 'POST':
        id_tarefa = request.POST.get('id_tarefa')
        tarefa = get_object_or_404(Tarefas, pk=id_tarefa)

        id_projeto = request.POST.get('id_projeto')
        projeto = get_object_or_404(Projeto, pk=id_projeto)

        id_colaboradores = request.POST.getlist('id_colaborador')
        
        form = CadEquipeTarefa(request.POST)
        if form.is_valid():
            for id_colaborador in id_colaboradores:
                equipes = Equipe.objects.filter(id_projeto=projeto, id_colaborador=id_colaborador)

                for equipe in equipes:
                    try:
                        nova_equipe_tarefa = Equipe_Tarefa(
                            id_tarefa=tarefa,
                            id_projeto=equipe,
                            id_colaborador=equipe
                        )
                        nova_equipe_tarefa.save()
                    except IntegrityError:
                        colaborador = equipe.id_colaborador
                        messages.error(request, f'O colaborador {colaborador} já está associado a esta tarefa.')
                        return redirect('cadastro_equipe_tarefa')
            
            messages.success(request, 'Equipe de tarefa cadastrada com sucesso')
            return redirect('/home_page/')
    else:
        form = CadEquipeTarefa()

    return render(request, 'cadastro_equipe_tarefa.html', {'form': form})


from django.shortcuts import render

def kanban(request, id):
    # Filtra as tarefas do projeto com o id fornecido
    tarefas_projeto = Tarefas.objects.filter(id_projeto__id_projeto=id)

    # Organiza as tarefas por status e inclui todos os campos
    tarefas_concluidas = [
        {
            'id_tarefa': tarefa.id_tarefa,
            'nome_tarefa': tarefa.nome_tarefa,
            'data_inicio': tarefa.data_inicio,
            'data_fim': tarefa.data_fim,
            'observacoes': tarefa.observacoes,
            'prioridade': tarefa.id_prioridade.nome_prioridade,
            'status': tarefa.id_status.nome_status,
            'projeto': tarefa.id_projeto.nome_projeto,
        }
        for tarefa in tarefas_projeto.filter(id_status__nome_status='CONCLUIDO')
    ]

    tarefas_pendentes = [
        {
            'id_tarefa': tarefa.id_tarefa,
            'nome_tarefa': tarefa.nome_tarefa,
            'data_inicio': tarefa.data_inicio,
            'data_fim': tarefa.data_fim,
            'observacoes': tarefa.observacoes,
            'prioridade': tarefa.id_prioridade.nome_prioridade,
            'status': tarefa.id_status.nome_status,
            'projeto': tarefa.id_projeto.nome_projeto,
        }
        for tarefa in tarefas_projeto.filter(id_status__nome_status='PENDENTE')
    ]

    tarefas_em_andamento = [
        {
            'id_tarefa': tarefa.id_tarefa,
            'nome_tarefa': tarefa.nome_tarefa,
            'data_inicio': tarefa.data_inicio,
            'data_fim': tarefa.data_fim,
            'observacoes': tarefa.observacoes,
            'prioridade': tarefa.id_prioridade.nome_prioridade,
            'status': tarefa.id_status.nome_status,
            'projeto': tarefa.id_projeto.nome_projeto,
        }
        for tarefa in tarefas_projeto.filter(id_status__nome_status='EM ANDAMENTO')
    ]

    # Passa as tarefas para o template
    context = {
        'completed_tasks': tarefas_concluidas,
        'pending_tasks': tarefas_pendentes,
        'in_progress_tasks': tarefas_em_andamento,
    }

    return render(request, 'kanban.html', context)

def lista(request, id):
    # Filtra as tarefas do projeto com o id fornecido
    tarefas_projeto = Tarefas.objects.filter(id_projeto__id_projeto=id)
    form = CadTarefa()

    projeto = Projeto.objects.get(id_projeto=id)

    # Filtra as tarefas com base nos diferentes status
    tarefas_concluidas = tarefas_projeto.filter(id_status__nome_status='CONCLUIDO')
    tarefas_pendentes = tarefas_projeto.filter(id_status__nome_status='PENDENTE')
    tarefas_em_andamento = tarefas_projeto.filter(id_status__nome_status='EM ANDAMENTO')

    # Buscar todos os status disponíveis
    todos_status = Status.objects.all()

    # Buscar todas as prioridades disponíveis
    todas_prioridades = Prioridade.objects.all()  # Certifique-se de que Prioridade está importado

    # Passa as tarefas e opções para o template
    context = {
        'form': form,
        'completed_tasks': tarefas_concluidas,
        'pending_tasks': tarefas_pendentes,
        'in_progress_tasks': tarefas_em_andamento,
        'projeto': projeto,
        'status_choices': todos_status,  # Lista de status
        'priority_choices': todas_prioridades  # Lista de prioridades
    }

    return render(request, 'lista.html', context)


def descricao_projeto(request, id):
    projeto = get_object_or_404(Projeto, id_projeto=id)
    documentos = Documento.objects.filter(id_projeto=projeto)
    
    equipe = Equipe.objects.filter(id_projeto=projeto).select_related('id_colaborador')
    equipe_ids = equipe.values_list('id_colaborador', flat=True)
    colaboradores_disponiveis = Colaborador.objects.exclude(id_colaborador__in=equipe_ids)

    if request.method == 'POST':
        colaboradores_ids = request.POST.getlist('colaboradores')
        
        # Remove os colaboradores que não estão mais na lista de IDs fornecida
        Equipe.objects.filter(id_projeto=projeto).exclude(id_colaborador__in=colaboradores_ids).delete()
        
        # Adiciona os novos colaboradores
        for colaborador_id in colaboradores_ids:
            colaborador = Colaborador.objects.get(id_colaborador=colaborador_id)
            Equipe.objects.get_or_create(id_projeto=projeto, id_colaborador=colaborador)

        messages.success(request, 'Equipe atualizada com sucesso!')
        return redirect('descricao_projeto', id=projeto.id_projeto)
    
    return render(request, 'desc_proj.html', {
        'projeto': projeto,
        'documentos': documentos,
        'equipe': equipe,
        'colaboradores_disponiveis': colaboradores_disponiveis,
    })


def update_task(request, id_task, id_status):
    # Obtém a tarefa ou retorna 404 se não encontrada
    tarefa = get_object_or_404(Tarefas, id_tarefa=id_task)
    
    # Atualiza o status da tarefa
    tarefa.id_status_id = id_status  # Atualiza o status
    projeto_id = tarefa.id_projeto.id_projeto  # Salva o ID do projeto em outra variável
    tarefa.save()  # Salva as alterações no banco de dados

    # Você pode usar `projeto_id` conforme necessário
    print("ID do projeto associado:", projeto_id)

    return redirect(f'/kanban/{projeto_id}')


def editar_tarefa(request):
    if request.method == 'POST':
        tarefa_id = request.POST.get('tarefa_id')
        nome_tarefa = request.POST.get('nome_tarefa')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        prioridade_id = request.POST.get('prioridade')
        status_id = request.POST.get('status')
        observacoes = request.POST.get('observacoes')

        tarefa = get_object_or_404(Tarefas, id_tarefa=tarefa_id)
        prioridade = Prioridade.objects.get(id_prioridade=prioridade_id)
        status = Status.objects.get(id_status=status_id)

        tarefa.nome_tarefa = nome_tarefa
        tarefa.data_inicio = data_inicio
        tarefa.data_fim = data_fim
        tarefa.id_prioridade = prioridade
        tarefa.id_status = status
        tarefa.observacoes = observacoes
        tarefa.save()

        return redirect('lista_tarefas', id=tarefa.id_projeto.id_projeto)  # Redireciona de volta para a página de tarefas

def remover_colaborador(request, id_equipe):
    equipe = get_object_or_404(Equipe, id_equipe=id_equipe)
    equipe.delete()
    messages.success(request, 'Colaborador removido da equipe com sucesso.')
    return redirect('descricao_projeto', id=equipe.id_projeto.id_projeto)

    
def dashboard(request):
    return render(request, 'dashboard.html') 


def task_details(request, task_id):
    try:
        # Tenta obter a tarefa com o ID fornecido
        tarefa = Tarefas.objects.get(id_tarefa=task_id)

        # Acessando as informações associadas às ForeignKeys
        task = {
            'nome_tarefa': tarefa.nome_tarefa,
            'data_inicio': tarefa.data_inicio,
            'data_fim': tarefa.data_fim,
            'observacoes': tarefa.observacoes,
            'prioridade': tarefa.id_prioridade.nome_prioridade,  # Acessando o nome da prioridade
            'status': tarefa.id_status.nome_status,  # Acessando o nome do status
            'projeto': tarefa.id_projeto.nome_projeto,  # Acessando o nome do projeto
        }

        return JsonResponse(task)

    except Tarefas.DoesNotExist:
        return JsonResponse({'error': 'Tarefa não encontrada'}, status=404)