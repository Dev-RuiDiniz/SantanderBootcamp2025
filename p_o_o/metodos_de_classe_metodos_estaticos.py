# Metodos de Classe e Métodos Estáticos
# Métodos de classe e métodos estáticos são usados para definir comportamentos que não dependem do estado da instância, mas sim da classe ou de um contexto específico.

class Exemplo:
    contador = 0  # variável de classe

    def __init__(self):
        Exemplo.contador += 1

    @classmethod
    def obter_contador(cls):
        return cls.contador

    @staticmethod
    def mensagem_boas_vindas():
        return "Bem-vindo ao exemplo de métodos de classe e estáticos!"

# Exemplo de uso
obj1 = Exemplo()
obj2 = Exemplo()
print(Exemplo.obter_contador())  # Saída: 2
print(Exemplo.mensagem_boas_vindas())  # Saída: Bem-vindo ao exemplo de métodos de classe e estáticos!  
# O método de classe `obter_contador` acessa a variável de classe `contador`, enquanto o método estático `mensagem_boas_vindas` não depende de nenhuma instância ou classe específica.
# Ambos os métodos demonstram como podemos organizar comportamentos relacionados à classe sem depender de instâncias específicas.
# Isso é útil para criar métodos que podem ser chamados diretamente na classe, sem a necessidade de criar uma instância, e para agrupar comportamentos que são relevantes para a classe como um todo.
