# Iteradores em Python são objetos que permitem percorrer uma coleção de elementos, como listas, tuplas ou dicionários, sem precisar conhecer a estrutura interna da coleção. Eles implementam os métodos `__iter__()` e `__next__()`, permitindo que sejam usados em loops `for` e outras construções que requerem iteração.
class MeuIterador:
    """
    Um exemplo simples de um iterador que gera números de 0 a n-1.
    """

    def __init__(self, n):
        self.n = n
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.n:
            resultado = self.atual
            self.atual += 1
            return resultado
        else:
            raise StopIteration
        
# Exemplo de uso do iterador
if __name__ == "__main__":
    meu_iterador = MeuIterador(5)
    for numero in meu_iterador:
        print(numero)
# Neste exemplo, a classe `MeuIterador` implementa um iterador que gera números de 0 a n-1.
# O método `__iter__()` retorna o próprio iterador, e o método `__next__()` retorna o próximo número na sequência, levantando `StopIteration` quando não há mais números a serem gerados.
# O iterador pode ser usado em um loop `for`, que chama automaticamente os métodos `__iter__()` e `__next__()` para percorrer os elementos.