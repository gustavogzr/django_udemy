from django.contrib.auth.models import User, UserManager # importa os modelos de usuário e o gerenciador de usuário

dir(User) # apresenta os atributos e métodos do modelo de usuário
help(User) # apresenta a documentação do modelo de usuário
help(User.save) # apresenta a documentação do método create do modelo de usuário

dir(UserManager) # apresenta os atributos e métodos do gerenciador de usuário
help(UserManager) # apresenta a documentação do gerenciador de usuário

usuario = User.objects.create_user(username='teste',password='123456',email='teste@gmail.com') # cria um usuário, mas não salva no banco de dados
usuario.save() # salva o usuário no banco de dados

ret = User.objects.all() # recupera todos os usuários do banco de dados
ret # apresenta os usuários recuperados
ret[0] # apresenta o primeiro usuário recuperado
ret[0].username # apresenta o nome do primeiro usuário recuperado
ret[0].password # apresenta a senha criptografada do primeiro usuário recuperado
ret[0].email # apresenta o email do primeiro usuário recuperado
ret[0].first_name # apresenta o primeiro nome do primeiro usuário recuperado
ret[0].last_name # apresenta o último nome do primeiro usuário recuperado

user = User.objects.get(pk = 1) # recupera o usuário com a chave primária igual a 1
user # apresenta o usuário recuperado

user.first_name = 'João' # altera o primeiro nome do usuário
user.last_name = 'da Silva' # altera o último nome do usuário
user.save() # salva as alterações no banco de dados

ret2 = User.objects.get(id = 1) # recupera o usuário com o id igual 1

ret2.first_name # apresenta o primeiro nome do usuário recuperado
ret2.last_name # apresenta o último nome do usuário recuperado

felicity = User.objects.create_user(username='felicity',password='123456',email='felicity@gmail.com',first_name='Felicity',last_name='Jones') # cria um usuário com os dados informados
felicity.save() # salva o usuário no banco de dados

fefe = User.objects.get(username='felicity') # recupera o usuário com o nome de usuário igual a 'felicity'
fefe # apresenta o usuário recuperado
fefe.first_name # apresenta o primeiro nome do usuário recuperado

angelina = User.objects.create_user(username='angelina',password='123456',email='angelina@gmail.com',is_staff=True) # cria um usuário com os dados informados e com permissão de staff
angelina.save() # salva o usuário no banco de dados

adm = User.objects.create_user(username='darth',password='123456',email='darth@darkstar.com',is_staff=True,is_superuser=True) # cria um usuário com os dados informados e com permissão de staff e superusuário
adm.save() # salva o usuário no banco de dados