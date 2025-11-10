from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Número do chassi do carro. Máximo de 16 caracteres.')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'
        
    def __str__(self):
        return self.numero
    
class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome da montadora. Máximo de 30 caracteres.')

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'
    
    def __str__(self):
        return self.nome

def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0] # Retorna a montadora padrão, criando-a se não existir
    # get_or_create retorna uma tupla (objeto, criado), por isso o [0] para pegar apenas o objeto. O criado retornará True se o objeto foi criado, False se já existia.

class Carro(models.Model):
    """
    # One to One Relationship:
    Cada carro só pode se relacionar com um chassi
    e cada chassi só pode se relacionar com um carro.

    # Many to One Relationship (Foreign Key):
    Cada carro está associado a uma montadora,
    mas uma montadora pode ter vários carros.

    # Many to Many Relationship:
    Cada carro pode ser dirigido por vários motoristas,
    e cada motorista pode dirigir vários carros.
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE) # Relacionamento Um para Um

    # montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE) 
    # Exemplo com CASCADE: se a montadora for deletada, os carros associados também serão deletados
    # montadora = models.ForeignKey(Montadora, on_delete=models.SET_DEFAULT, default=1)
    # Exemplo com SET_DEFAULT: se a montadora for deletada, os carros associados terão a montadora padrão (id=1)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
    # Exemplo com SET: se a montadora for deletada, os carros associados terão a montadora definida pela função set_default_montadora
    
    motoristas = models.ManyToManyField(get_user_model()) # Relacionamento Muitos para Muitos
    modelo = models.CharField('Modelo', max_length=30, help_text='Modelo do carro. Máximo de 30 caracteres.')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def __str__(self):
        return f'{self.montadora} {self.modelo}'