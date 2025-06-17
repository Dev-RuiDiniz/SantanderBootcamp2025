# Extruturas condicionais são usadas para tomar decisões no código, permitindo que diferentes blocos de código sejam executados com base em condições específicas.
# As estruturas condicionais mais comuns em Python são `if`, `elif` e `else`. Elas permitem que você execute diferentes partes do código dependendo de condições booleanas.

# A sintaxe básica é a seguinte:
# if <condição>:
#     <bloco de código se a condição for verdadeira>
# elif <outra condição>:
#     <bloco de código se a outra condição for verdadeira>
# else:
#     <bloco de código se nenhuma das condições anteriores for verdadeira>

# Exemplo de uso de estruturas condicionais
def verificar_numero(num):
    if num > 0:
        return "O número é positivo."
    elif num < 0:
        return "O número é negativo."
    else:
        return "O número é zero."


