# Estruturas de repetição são usadas para executar um bloco de código várias vezes, com base em uma condição ou em uma sequência de elementos. As estruturas de repetição mais comuns em Python são `for` e `while`.

# A estrutura `for` é usada para iterar sobre uma sequência (como uma lista, tupla ou string) ou um objeto iterável. A sintaxe básica é:
# for <variável> in <sequência>:
#     <bloco de código a ser executado para cada elemento da sequência>
# # Exemplo de uso da estrutura `for`
def imprimir_numeros(lista):
    for numero in lista:
        print(numero)
        
# A estrutura `while` é usada para executar um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é:
# while <condição>:
#     <bloco de código a ser executado enquanto a condição for verdadeira>
# # Exemplo de uso da estrutura `while`
def contar_ate_dez():
    contador = 1
    while contador <= 10:
        print(contador)
        contador += 1
# Exemplo de uso de ambas as estruturas de repetição
def exemplo_repeticoes():
    numeros = [1, 2, 3, 4, 5]
    print("Imprimindo números com for:")
    imprimir_numeros(numeros)
    
    print("\nContando até dez com while:")
    contar_ate_dez()    
    
# Chamada da função de exemplo
exemplo_repeticoes()
# Este código demonstra o uso de estruturas de repetição em Python, incluindo `for` e `while`.
# Ele define duas funções: `imprimir_numeros` e `contar_ate_dez`, que utilizam essas estruturas para iterar sobre uma lista de números e contar até dez, respectivamente. A função `exemplo_repeticoes` chama ambas as funções para mostrar como elas funcionam em conjunto.
