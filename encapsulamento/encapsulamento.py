# Encapsulamento é o conceito de esconder os detalhes internos de uma classe, expondo apenas o que é necessário para o usuário da classe.
# Para implementar encapsulamento em Python, usamos convenções de nomenclatura para indicar a visibilidade dos atributos e métodos:
# - Atributos e métodos públicos: acessíveis de fora da classe, nomeados normalmente
# - Atributos e métodos protegidos: acessíveis apenas dentro da classe e subclasses, nomeados com um underscore prefixado (ex: _atributo)
# - Atributos e métodos privados: acessíveis apenas dentro da classe, nomeados com dois underscores prefixados (ex: __atributo)

#exemplo de encapsulamento
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError("Saldo não pode ser negativo.")
    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.__saldo}"
# Exemplo de uso
if __name__ == "__main__":
    conta = ContaBancaria("João", 1000)
    print(conta)
    conta.depositar(500)
    print(conta)
    conta.sacar(200)
    print(conta)
    conta.set_saldo(1500)
    print(conta)
    