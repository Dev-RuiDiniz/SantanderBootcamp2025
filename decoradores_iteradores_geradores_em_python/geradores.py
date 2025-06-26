# Geradores em Python são uma forma especial de iteradores que permitem criar sequências de valores sob demanda, usando a palavra-chave `yield`. Eles são mais simples de escrever do que os iteradores tradicionais, pois não requerem a implementação dos métodos `__iter__()` e `__next__()`. Em vez disso, um gerador é uma função que usa `yield` para retornar valores um de cada vez, permitindo que o estado da função seja mantido entre as chamadas.

def meu_gerador(n):
    """
    Um gerador que produz números de 0 a n-1.
    """
    for i in range(n):
        yield i
# Exemplo de uso do gerador
if __name__ == "__main__":
    for numero in meu_gerador(5):
        print(numero)
# Neste exemplo, a função `meu_gerador` é um gerador que produz números de 0 a n-1.
# A palavra-chave `yield` permite que a função retorne um valor e pause sua execução,
# mantendo seu estado. Quando o gerador é chamado novamente, ele retoma a execução a partir do ponto onde foi pausado, continuando a gerar os próximos valores.
# Os geradores são uma maneira eficiente de trabalhar com sequências grandes ou infinitas, pois eles geram valores sob demanda, economizando memória e processamento.