from django.contrib import admin
from .models import Carro, Chassi, Montadora

# Register your models here.

@admin.register(Montadora) # o @ serve para registrar o modelo na interface admin
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')

    def get_motoristas(self, obj):
        return ", ".join([motorista.username for motorista in obj.motoristas.all()])

    get_motoristas.short_description = 'Motoristas' # Define o nome da coluna na interface admin