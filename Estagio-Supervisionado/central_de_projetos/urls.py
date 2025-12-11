from django.urls import path
from . import views

urlpatterns = [
        path('', views.login, name='login'),
        path('home_page/', views.home_page, name='home_page'),
        path('criar_projetos/', views.criar_projetos, name='criar_projetos'),
        path('cad_colaborador/', views.cadastro_colaborador, name='cadastro_colaborador'),
        path('cad_equipe/', views.cadastro_equipe, name='cadastro_equipe'),
        path('cad_tarefa/', views.cadastro_tarefa, name='cadastro_tarefa'),
        path('cad_tarefa_equipe/', views.cadastro_equipe_tarefa, name='cadastro_equipe_tarefa'),
        path('ver_projetos/', views.ver_projetos, name='ver_projetos'),
        path('colaborador', views.colaborador, name='colaborador'),
        path('projeto', views.projeto, name='projeto'),
        path('equipe', views.equipe, name='equipe'),
        path('tarefa', views.tarefa, name='tarefa'),
        path('equipetarefa', views.equipetarefa, name='equipetarefa'),
        path('sair/', views.sair, name='sair'),
        path('desc_proj', views.descricao_projeto, name='descricao_projeto'),
        path('kanban/<int:id>/', views.kanban, name='kanban'),
        path('desc_proj/<int:id>/', views.descricao_projeto, name='descricao_projeto'),
        path('update_task/<int:id_task>/<int:id_status>', views.update_task, name='update_task'),
        path('lista/<int:id>/', views.lista, name='lista'),
        path('editar_tarefa', views.editar_tarefa, name='editar_tarefa'),
        path('remover_colaborador/<int:id_equipe>/', views.remover_colaborador, name='remover_colaborador'),
        path('dashboard', views.dashboard, name='dashboard'),
        path('task_details/<int:task_id>/', views.task_details, name='task_details'),
        path('lista_tarefas/<int:id>/', views.lista, name='lista_tarefas'),  # Confirme que o nome está correto

]