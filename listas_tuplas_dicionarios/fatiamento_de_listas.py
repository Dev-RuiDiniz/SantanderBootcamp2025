# fatiamento de listas é uma técnica que permite acessar partes específicas de uma lista em Python.
# Isso é feito usando a notação de fatiamento, que permite especificar um intervalo de índices para extrair elementos da lista.
# O fatiamento é uma ferramenta poderosa para manipular listas, permitindo acessar sublistas, modificar partes da lista e muito mais.

# Exemplo de fatiamento de listas em Python
def fatiamento_de_listas():
    # Criando uma lista de números
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Fatiando a lista para obter os primeiros cinco elementos
    primeiros_cinco = numeros[:5]
    print("Primeiros cinco elementos:", primeiros_cinco)
    
    # Fatiando a lista para obter os últimos cinco elementos
    ultimos_cinco = numeros[-5:]
    print("Últimos cinco elementos:", ultimos_cinco)
    
    # Fatiando a lista para obter elementos do meio
    meio = numeros[3:7]
    print("Elementos do meio (índices 3 a 6):", meio)
    
    # Fatiando a lista com um passo
    passo = numeros[::2]
    print("Elementos com passo 2:", passo)
    
# Chamada da função de fatiamento de listas
fatiamento_de_listas()