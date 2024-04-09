from django.urls import get_resolver 
from pprint import pprint # print alternativo para visualizar melhor os resultados

pprint(get_resolver().url_patterns[0].url_patterns) # imprime a lista de urls do projeto