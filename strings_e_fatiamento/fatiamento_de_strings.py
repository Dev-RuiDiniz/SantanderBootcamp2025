# Fatiamento de strings
# Fatiamento de strings é uma técnica que permite extrair partes de uma string usando índices e intervalos. Em Python, isso é feito utilizando a notação de colchetes `[]` com o formato `string[inicio:fim:passo]`, onde `inicio` é o índice inicial, `fim` é o índice final (não incluído), e `passo` é o intervalo entre os índices.

def fatiamento_de_strings():
    texto = "Python é uma linguagem de programação poderosa e versátil."
    
    # Fatiamento básico
    fatiado1 = texto[0:6]  # Extrai "Python"
    fatiado2 = texto[7:9]  # Extrai "é uma"
    
    # Fatiamento com passo
    fatiado3 = texto[0:30:5]  # Extrai "Pto nlgm o o e"
    
    # Fatiamento negativo
    fatiado4 = texto[-9:]  # Extrai "versátil."
    
    # Fatiamento completo
    fatiado5 = texto[:]  # Extrai a string completa
    
    print("Fatiamento básico:", fatiado1, fatiado2)
    print("Fatiamento com passo:", fatiado3)
    print("Fatiamento negativo:", fatiado4)
    print("Fatiamento completo:", fatiado5)
    
# Chamada da função de fatiamento
fatiamento_de_strings()
# Este código demonstra o fatiamento de strings em Python, mostrando como extrair partes específicas de uma string usando índices e intervalos. Ele inclui exemplos de fatiamento básico, com passo, negativo e completo, e imprime os resultados.