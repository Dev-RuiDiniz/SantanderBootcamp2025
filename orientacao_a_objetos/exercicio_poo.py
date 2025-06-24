# Crie um classe bicicleta que represente uma bicicleta, com atributos como marca, modelo e cor. Implemente métodos para exibir as informações da bicicleta e para simular o ato de pedalar.

class Bicicleta:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def exibir_informacoes(self):
        return f"Bicicleta - Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}"

    def pedalar(self):
        return f"Pedalando a bicicleta {self.modelo} da marca {self.marca}."
    
# Exemplo de uso da classe Bicicleta
bicicleta1 = Bicicleta("Caloi", "Elite", "Vermelha")
print(bicicleta1.exibir_informacoes())  # Saída: Bicicleta - Marca: Caloi, Modelo: Elite, Cor: Vermelha
print(bicicleta1.pedalar())  # Saída: Pedalando a bicicleta Elite da marca Caloi.

# Crie uma classe Livro que represente um livro, com atributos como título, autor e ano de publicação. Implemente métodos para exibir as informações do livro e para simular a leitura do livro.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_informacoes(self):
        return f"Livro - Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}"

    def ler(self):
        return f"Lendo o livro '{self.titulo}' do autor {self.autor}."
# Exemplo de uso da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
print(livro1.exibir_informacoes())  # Saída: Livro - Título: Dom Casmurro, Autor: Machado de Assis, Ano de Publicação: 1899
print(livro1.ler())  # Saída: Lendo o livro 'Dom Casmurro' do autor Machado de Assis.