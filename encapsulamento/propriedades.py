# Propriedades em Python
# Propriedades são uma forma de encapsulamento que permite controlar o acesso a atributos de uma classe.
# Elas permitem que você defina métodos para obter (getter) e definir (setter) o valor de um atributo, sem expor diretamente o atributo.

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            raise ValueError("O preço deve ser positivo.")

# Exemplo de uso
if __name__ == "__main__":
    produto = Produto("Laptop", 2500)
    print(produto.nome)
    print(produto.preco)
    produto.preco = 3000
    print(produto.preco)