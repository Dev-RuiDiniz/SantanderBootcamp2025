# Recursos Públicos ou Privados são conceitos que ajudam a entender o acesso e a visibilidade de atributos e métodos em uma classe. Recursos públicos são acessíveis de fora da classe, enquanto recursos privados são restritos à própria classe.
# Em Python, não há modificadores de acesso como em outras linguagens (ex: public, private), mas usamos convenções de nomenclatura para indicar a visibilidade dos recursos:
# - Recursos Públicos: Atributos e métodos acessíveis de fora da classe, nomeados normalmente.
# - Recursos Privados: Atributos e métodos acessíveis apenas dentro da classe, nomeados com dois underscores prefixados (ex: __atributo).

# Exemplo de Recursos Públicos e Privados
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo  # Recurso público
        self.__ano = ano      # Recurso privado

    def mostrar_informacoes(self):
        return f"Modelo: {self.modelo}, Ano: {self.__ano}"

    def __ano_atual(self):
        return 2023 - self.__ano  # Método privado
    def mostrar_idade(self):
        return f"O carro {self.modelo} tem {self.__ano_atual()} anos."
# Exemplo de uso
if __name__ == "__main__":
    carro = Carro("Fusca", 1970)
    print(carro.mostrar_informacoes())
    print(carro.mostrar_idade())