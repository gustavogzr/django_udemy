# usando a biblioteca Translate

# pip install translate

from translate import Translator # Importa a biblioteca Translate

translator_pt_to_en = Translator(from_lang="pt", to_lang="en") # Cria um objeto Translator para inglês
translator_pt_to_es = Translator(from_lang="pt", to_lang="es") # Cria um objeto Translator para espanhol

texto = "Python é uma linguagem de programação de alto nível." # Cria um texto

print(translator_pt_to_en.translate(texto)) # Traduz o texto para inglês
print(translator_pt_to_es.translate(texto)) # Traduz o texto para espanhol