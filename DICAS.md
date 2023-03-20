# Dicas de Comandos

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
python manage.py createsuperuser *criar admin*
python manage.py shell *carrega um console Python*
python manage.py collectstatic *junta os arquivos estáticos (css, js, imagens etc) em uma única pasta*

pip freeze > requirements.txt *salvar versões das bibliotecas*
pip install -r requirements.txt *instalar todos os apps do arquivo requirements.txt*

touch .gitignore *criar arquivo .gitignore para ignorar pasta e arquivos*

https://www.heroku.com/ *publicar site*
https://devcenter.heroku.com/articles/getting-started-with-python *baixar instalador para o computador*
heroku login *comando para abrir a tela de login*
heroku create django1-gzr --buildpack heroku/python *criar instância web*