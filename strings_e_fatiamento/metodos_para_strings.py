# Metodos uteis para manipulação de strings
# Métodos úteis para manipulação de strings em Python incluem `upper()`, `lower()`, `strip()`, `replace()`, `find()`, `split()`, e `join()`. Esses métodos permitem transformar, limpar, buscar e manipular strings de maneira eficiente.

# Exemplos:
def exemplo_metodos_strings():
    texto = "  Olá, Mundo!  "
    
    # Convertendo para maiúsculas
    print("Maiúsculas:", texto.upper())
    
    # Convertendo para minúsculas
    print("Minúsculas:", texto.lower())
    
    # Removendo espaços em branco no início e no final
    print("Sem espaços:", texto.strip())
    
    # Substituindo uma parte da string
    print("Substituído:", texto.replace("Mundo", "Python"))
    
    # Encontrando a posição de uma substring
    posicao = texto.find("Mundo")
    print("Posição de 'Mundo':", posicao)
    
    # Dividindo a string em uma lista
    lista = texto.split(", ")
    print("Dividido em lista:", lista)
    
    # Juntando uma lista em uma string
    nova_string = " - ".join(lista)
    print("Juntado com '-':", nova_string)
    
# Chamada da função de exemplo
exemplo_metodos_strings()
