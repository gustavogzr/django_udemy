from django.db import models

from django.contrib.auth.models import AbstractBaseUser # importa o modelo base de usuário abstrato
from django.contrib.auth.models import AbstractUser, BaseUserManager # importa o modelo de usuário abstrato

# o AbstractBaseUser é um modelo de usuário abstrato que não possui campos de nome de usuário, email, primeiro nome e último nome, ou seja, é um modelo mais simplório em relação ao AbstractUser

# o BaseUserManager é um gerenciador de usuário que possui métodos para criar usuários, criar superusuários, criar usuários comuns, entre outros

class UsuarioManager(BaseUserManager):
    use_in_migrations = True # indica que o gerenciador de usuário será utilizado nas migrações

    def _create_user(self, email, password, **extra_fields): # método para criar um usuário comum
        if not email: 
            raise ValueError('O email é obrigatório') # lança uma exceção se o email não for informado
        email = self.normalize_email(email) # normaliza o email
        user =  self.model(email=email, username=email, **extra_fields) # cria um usuário com o email, nome de usuário e campos extras informados
        user.set_password(password) # define a senha do usuário
        user.save(using=self._db) # salva o usuário no banco de dados
        return user
    
    def create_user(self, email, password=None, **extra_fields): # método para criar um usuário comum
        extra_fields.setdefault('is_staff', True) # define que o usuário é staff
        extra_fields.setdefault('is_superuser', False) # define que o usuário não é superusuário
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields): # método para criar um superusuário
        extra_fields.setdefault('is_staff', True) # define que o usuário é staff
        extra_fields.setdefault('is_superuser', True) # define que o usuário é superusuário

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True.') # lança uma exceção se o usuário não for superusuário
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True.') # lança uma exceção se o usuário não for staff
        
        return self._create_user(email, password, **extra_fields) # cria um superusuário
    


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True) # campo de email
    fone = models.CharField('Telefone', max_length=15) # campo de telefone
    is_staff = models.BooleanField('Membro da Equipe', default=True) # campo de staff

    USERNAME_FIELD = 'email' # campo de email como nome de usuário
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone'] # campos obrigatórios. O e-mail e a senha são obrigatórios por padrão porque são utilizados para acesso ao sistema


    def __str__(self):
        return self.email
    
    objects = UsuarioManager()

# Create your models here.
