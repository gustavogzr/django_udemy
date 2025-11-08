from django.db import models

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
    
class Carro(models.Model):
    """
    # One to One Relationship:
    Cada carro só pode se relacionar com um chassi
    e cada chassi só pode se relacionar com um carro.

    # Many to One Relationship (Foreign Key):
    Cada carro está associado a uma montadora,
    mas uma montadora pode ter vários carros.
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE) # Relacionamento Um para Um
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE) # Relacionamento Muitos para Um
    modelo = models.CharField('Modelo', max_length=30, help_text='Modelo do carro. Máximo de 30 caracteres.')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def __str__(self):
        return f'{self.montadora} {self.modelo}'