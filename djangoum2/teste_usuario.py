from django.contrib.auth.models import User # importa os modelos de usuário e o gerenciador de usuário

dir(User) # apresenta os atributos e métodos do modelo de usuário

fefe = User.objects.get(pk = 2) # recupera o usuário com a chave primária igual a 2

fefe.get_full_name() # apresenta o nome completo do usuário recuperado