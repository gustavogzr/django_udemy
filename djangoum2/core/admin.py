from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import Post

# Register your models here.

@admin.register(Post) # registra o modelo Post no admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo','_autor'] # apresenta os campos título e autor na listagem

    exclude = ['autor',] # exclui o campo autor do formulário

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}' # retorna o nome completo do autor
    
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request) # recupera a query
        return qs.filter(autor=request.user) if not request.user.is_superuser else qs # filtra os posts pelo autor se o usuário não for superusuário
    
    def save_model(self, request, obj, form, change): # sobrescreve o método save_model
        obj.autor = request.user # define o autor do post como o usuário logado
        super().save_model(request, obj, form, change) # salva o post no banco de dados