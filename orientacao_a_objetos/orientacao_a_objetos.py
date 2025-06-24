# Paradigma da Orientação a Objetos (OO) é um paradigma de programação que utiliza objetos e classes para organizar o código. Ele é baseado em conceitos como encapsulamento, herança e polimorfismo, permitindo uma abordagem modular e reutilizável no desenvolvimento de software.

#         return f"Olá, {nome}!"
#     # Chamando a função decorada
#     resultado = saudacao("Mundo")
#     print(resultado)

# Definindo uma classe simples para representar um objeto
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Exemplo de herança
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        return f"{super().apresentar()} Estou estudando {self.curso}."

# Exemplo de polimorfismo
def apresentar_pessoa(pessoa):
    print(pessoa.apresentar())
# Função principal para demonstrar o paradigma de orientação a objetos
def orientacao_a_objetos():
    pessoa1 = Pessoa("Alice", 30)
    estudante1 = Estudante("Bob", 20, "Engenharia")

    apresentar_pessoa(pessoa1)
    apresentar_pessoa(estudante1)
# Chamada da função de orientação a objetos
orientacao_a_objetos()