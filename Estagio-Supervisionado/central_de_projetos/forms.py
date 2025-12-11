from django.utils import timezone
from django import forms
from .models import Gerencia, Projeto, Colaborador, Equipe, Eixo, Prioridade, Objetivo, Status, Tarefas, Cargo

class CadColaborador(forms.Form):
    nome = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    id_cargo = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    especialidade = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    senha = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    id_gerencia = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        super(CadColaborador, self).__init__(*args, **kwargs)
        # Carregar as opções de Gerencia dinamicamente
        self.fields['id_gerencia'].choices = [('0', '---Selecione---')] + [
            (gerencia.id_gerencia, gerencia.nome) for gerencia in Gerencia.objects.all()
        ]
        self.fields['id_cargo'].choices = [('0', '---Selecione---')] + [
            (cargo.id_cargo, cargo.nome) for cargo in Cargo.objects.all()
        ]

class CadProjeto(forms.Form):
    nome_projeto = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',  # Mostra o seletor de data padrão do HTML5
            'class': 'form-control',  # Adiciona classes CSS customizadas
            'placeholder': 'Selecione a data de início'
        }),
        initial=timezone.now().date(),  # Define a data de hoje como inicial
        label='Data de Início'
        )
    data_fim = forms.DateField( 
         widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Selecione a data de término'
        }),
        required=False,  # Campo opcional
        label='Data de Término'
    )
    id_eixo = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    id_objetivo = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    processo_sei = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    observacoes = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'class': 'form-control', "cols": "40", "rows": "4"})
    )
    def __init__(self, *args, **kwargs):
        super(CadProjeto, self).__init__(*args, **kwargs)
        
        id_fields = [name for name in self.fields if name.startswith('id_')]
        
        print("Campos que começam com 'id_':", id_fields)

        self.fields['id_eixo'].choices = [('0', '---Selecione---')] + [
            (eixo.id_eixo, eixo.nome_eixo) for eixo in Eixo.objects.all()
        ]
        self.fields['id_objetivo'].choices = [('0', '---Selecione---')] + [
            (objetivo.id_objetivo, objetivo.nome_objetivo) for objetivo in Objetivo.objects.all()
        ]
class CadEquipe(forms.Form):
    id_projeto = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    id_colaborador = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        super(CadEquipe, self).__init__(*args, **kwargs)
        # Carregar as opções de Projeto dinamicamente
        self.fields['id_projeto'].choices = [('0', '---Selecione---')] + [
            (projeto.id_projeto, projeto.nome_projeto) for projeto in Projeto.objects.all()
        ]

        self.fields['id_colaborador'].choices = [('0', '---Selecione---')] + [
            (colaborador.id_colaborador, colaborador.nome) for colaborador in Colaborador.objects.all()
        ]

class CadTarefa(forms.Form):

    nome_tarefa = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    id_projeto = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',  # Mostra o seletor de data padrão do HTML5
            'class': 'form-control',  # Adiciona classes CSS customizadas
            'placeholder': 'Selecione a data de início'
        }),
        initial=timezone.now().date(),  # Define a data de hoje como inicial
        label='Data de Início'
    )

    data_fim = forms.DateField( 
         widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Selecione a data de término'
        }),
        required=False,  # Campo opcional
        label='Data de Término'
    )

    id_prioridade = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    id_status = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    observacoes = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'class': 'form-control', "cols": "40", "rows": "4"})
    )

    def __init__(self, *args, **kwargs):
        super(CadTarefa, self).__init__(*args, **kwargs)
        
        # Obtenção dos campos que começam com 'id_'
        id_fields = [name for name in self.fields if name.startswith('id_')]
        
        print("Campos que começam com 'id_':", id_fields)

        self.fields['id_prioridade'].choices = [('0', '---Selecione---')] + [
            (prioridade.id_prioridade, prioridade.nome_prioridade) for prioridade in Prioridade.objects.all()
        ]

        self.fields['id_status'].choices = [('0', '---Selecione---')] + [
            (status.id_status, status.nome_status) for status in Status.objects.all()
        ]

        self.fields['id_projeto'].choices = [('0', '---Selecione---')] + [
            (projeto.id_projeto, projeto.nome_projeto) for projeto in Projeto.objects.all()
        ]

class CadEquipeTarefa(forms.Form):
    id_projeto = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Projeto'
    )
    
    id_tarefa = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Tarefa'
    )

    id_colaborador = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Colaborador'
    )

    def __init__(self, *args, **kwargs):
        projeto_id = kwargs.pop('projeto_id', None)  
        super(CadEquipeTarefa, self).__init__(*args, **kwargs)
        
        
        self.fields['id_projeto'].choices = [('0', '---Selecione um projeto---')] + [
            (projeto.id_projeto, projeto.nome_projeto) for projeto in Projeto.objects.all()
        ]

        