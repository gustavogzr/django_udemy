# Dicas de Comandos

## Comandos Gerais de Python e Django

python -m venv .venv *criar ambiente virtual*
.venv\Scripts\activate *ativar venv*

pip install django *instalar django*
django-admin startproject django1_project . *criar projeto django - não esquecer do ponto final*
django-admin startapp core *criar novo app com nome core*
LANGUAGE_CODE = 'pt-br' *ajustar linguagem em settings*
TIME_ZONE = 'America/Sao_Paulo' *ajustar timezone*

python manage.py makemigrations *criar arquivo de migração de modelos*
python manage.py migrate *executa a migração dos modelos gerados via makemigrations*

python manage.py runserver *iniciar o servidor*
CTRL+C *parar servidor*
cls *limpar tela do cmd*

~~~bash
python manage.py createsuperuser # criar admin
python manage.py shell # carrega um console Python
python manage.py collectstatic # junta os arquivos estáticos (css, js, imagens etc) em uma única pasta
python manage.py test # executa os testes
~~~

pip freeze > requirements.txt *salvar versões das bibliotecas*
pip install -r requirements.txt *instalar todos os apps do arquivo requirements.txt*

touch .gitignore *criar arquivo .gitignore para ignorar pasta e arquivos*

<https://www.heroku.com/> *publicar site*
<https://devcenter.heroku.com/articles/getting-started-with-python> *baixar instalador para o computador*
heroku login *comando para abrir a tela de login*
heroku create django1-gzr --buildpack heroku/python *criar instância web*

## Testes do Django

Serão utilizadas as bibliotecas model_mommy e coverage para testes. O model_mommy é utilizado para criar objetos de teste e o coverage para verificar a cobertura dos testes. Para instalar as bibliotecas, execute os comandos abaixo:

~~~bash
pip install model_mommy coverage
~~~

Para usar o coverage, execute os comandos abaixo para rodar os testes, verificar o relatório de cobertura e abrir o relatório no navegador:

~~~bash
coverage run manage.py test
coverage report
coverage html
~~~

Para acessar os relatórios em HTML, acessa a pasta htmlcov e execute o seguinte comando:

~~~bash
python -m http.server
~~~

Para usar o model_mommy, realizar os comando abaixo:

~~~bash
python manage.py shell
~~~

~~~python
from model_mommy import mommy

cargo = mommy.make('core.Cargo') # cria um objeto de teste do model Cargo
cargo # exibe o objeto criado
cargo.cargo # exibe o nome do cargo criado automaticamente pelo model_mommy
cargo.cargo = "Gerente" # altera o nome do cargo
cargo.cargo # exibe o nome do cargo alterado
cargo.save() # salva o objeto no banco de dados

servicos = mommy.make('core.Servico', _quantity=5) # cria 5 objetos de teste do model Servico
servicos # exibe os objetos criados
servicos[0].servico # exibe o nome do serviço criado automaticamente pelo model_mommy
servicos[0].descricao # exibe a descrição do serviço criado automaticamente pelo model_mommy
servicos[0].icone # exibe o ícone do serviço criado automaticamente pelo model_mommy

funcionarios = mommy.make('core.Funcionario', _quantity=3) # cria 3 objetos de teste do model Funcionario
funcionarios # exibe os objetos criados
funcionarios[0] # exibe o objeto criado
funcionarios[0].cargo # exibe o cargo do funcionário criado automaticamente pelo model_mommy
~~~
