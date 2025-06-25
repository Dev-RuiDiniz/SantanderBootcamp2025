# Interfaces para POO são contratos que definem métodos que uma classe deve implementar. Elas permitem a criação de código mais flexível e reutilizável, pois diferentes classes podem implementar a mesma interface de maneiras distintas.

from abc import ABC, abstractmethod
class InterfaceExemplo(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        """Método que deve ser implementado por classes que herdam desta interface."""
        pass

    @staticmethod
    @abstractmethod
    def metodo_estatico():
        """Método estático que deve ser implementado por classes que herdam desta interface."""
        pass

    @classmethod
    @abstractmethod
    def metodo_de_classe(cls):
        """Método de classe que deve ser implementado por classes que herdam desta interface."""
        pass
class ImplementacaoExemplo(InterfaceExemplo):
    def metodo_abstracto(self):
        return "Implementação do método abstrato"

    @staticmethod
    def metodo_estatico():
        return "Implementação do método estático"

    @classmethod
    def metodo_de_classe(cls):
        return f"Implementação do método de classe na classe {cls.__name__}"

# Exemplo de uso
obj = ImplementacaoExemplo()
print(obj.metodo_abstracto())  # Saída: Implementação do método abstrato
print(ImplementacaoExemplo.metodo_estatico())  # Saída: Implementação do método estático
print(ImplementacaoExemplo.metodo_de_classe())  # Saída: Implementação do método de classe na classe ImplementacaoExemplo
# A classe `ImplementacaoExemplo` implementa a interface `InterfaceExemplo`, fornecendo implementações concretas para os métodos abstratos definidos na interface. Isso demonstra como as interfaces podem ser usadas para garantir que certas funcionalidades sejam implementadas, promovendo a consistência e a reutilização de código em diferentes classes.
# Interfaces são especialmente úteis em cenários onde diferentes classes precisam seguir um contrato comum, permitindo que o código funcione com qualquer classe que implemente a interface, sem precisar conhecer os detalhes de cada implementação específica. Isso é fundamental para a criação de sistemas flexíveis e extensíveis, onde novas funcionalidades podem ser adicionadas sem modificar o código existente.