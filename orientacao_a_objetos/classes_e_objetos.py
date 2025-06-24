# Classes e Objetos # Paradigma da Orientação a Objetos (OO) é um paradigma de programação que utiliza objetos e classes para organizar o código. Ele é baseado em conceitos como encapsulamento, herança e polimorfismo, permitindo uma abordagem modular e reutilizável no desenvolvimento de software.

# Classes:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos:
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

# Exemplo de uso:
print(pessoa1.apresentar())  # Saída: Olá, meu nome é Alice e eu tenho 30 anos.
print(pessoa2.apresentar())  # Saída: Olá, meu nome é Bob e eu tenho 25 anos.

# Herança:
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        return f"{super().apresentar()} Estou estudando {self.curso}."
    
# Exemplo de uso da classe Estudante:
estudante1 = Estudante("Carlos", 20, "Engenharia")
print(estudante1.apresentar())  # Saída: Olá, meu nome é Carlos e eu tenho 20 anos. Estou estudando Engenharia.