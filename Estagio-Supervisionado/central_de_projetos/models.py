from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Gerencia(models.Model):
    id_gerencia = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

class Especialidade(models.Model):
    id_especialidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

class ColaboradorManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        
        password = password or '1234'  
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if 'id_gerencia' not in extra_fields:
            try:
                # Busca a gerência específica chamada 'GERENTE'
                gerencia = Gerencia.objects.get(nome='GERENTE')
                extra_fields['id_gerencia'] = gerencia
            except Gerencia.DoesNotExist:
                raise ValueError("A gerência 'GERENTE' deve existir antes de criar um superusuário.")

        return self.create_user(email, password, **extra_fields)

class Colaborador(AbstractBaseUser, PermissionsMixin):
    id_colaborador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, default=1)
    especialidade = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    id_gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = ColaboradorManager()

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['nome']  


class Objetivo(models.Model):
    id_objetivo = models.AutoField(primary_key=True)
    nome_objetivo = models.CharField(max_length=255)

class Eixo(models.Model):
    id_eixo = models.AutoField(primary_key=True)
    nome_eixo = models.CharField(max_length=255)

class Projeto(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    nome_projeto = models.CharField(max_length=100)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    processo_sei = models.CharField(max_length=255)
    observacoes = models.CharField(max_length=255)
    id_objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    id_eixo = models.ForeignKey(Eixo, on_delete=models.CASCADE)

class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateField(auto_now_add=True)
    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

class Equipe(models.Model):
    id_equipe = models.AutoField(primary_key=True)
    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    id_colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_projeto', 'id_colaborador'],
                name='unique_projeto_colaborador'
            )
        ]

class Prioridade(models.Model):
    id_prioridade = models.AutoField(primary_key=True)
    nome_prioridade = models.CharField(max_length=255)

class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nome_status = models.CharField(max_length=255)


class Tarefas(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    nome_tarefa = models.CharField(max_length=255)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    observacoes = models.CharField(max_length=255)

    id_prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE)
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

class Equipe_Tarefa(models.Model):
    id_equipe_tarefa = models.AutoField(primary_key=True)
    id_tarefa = models.ForeignKey(Tarefas, on_delete=models.CASCADE)
    id_projeto = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='projeto_equipes')
    id_colaborador = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='colaborador_equipes')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_tarefa', 'id_projeto', 'id_colaborador'],
                name='unique_equipe_tarefa'
            )
        ]

class Documento_tarefa(models.Model):
    id_documento = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/tarefas')
    uploaded_at = models.DateField(auto_now_add=True)
    id_tarefa = models.ForeignKey(Tarefas, on_delete=models.CASCADE)
    