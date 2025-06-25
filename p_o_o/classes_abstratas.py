# Classes abstratas em Python são usadas para definir uma interface comum para um grupo de subclasses, permitindo que essas subclasses implementem métodos específicos. Elas são úteis quando você deseja garantir que certas funcionalidades sejam implementadas em todas as subclasses, mas não deseja fornecer uma implementação padrão na classe base.

from abc import ABC, abstractmethod
class ClasseAbstrata(ABC):
    @abstractmethod
    def metodo_abstrato(self):
        """Método que deve ser implementado por subclasses."""
        pass

    @staticmethod
    @abstractmethod
    def metodo_estatico():
        """Método estático que deve ser implementado por subclasses."""
        pass

    @classmethod
    @abstractmethod
    def metodo_de_classe(cls):
        """Método de classe que deve ser implementado por subclasses."""
        pass
class Subclasse(ClasseAbstrata):
    def metodo_abstrato(self):
        return "Implementação do método abstrato na subclasse"

    @staticmethod
    def metodo_estatico():
        return "Implementação do método estático na subclasse"

    @classmethod
    def metodo_de_classe(cls):
        return f"Implementação do método de classe na subclasse {cls.__name__}"
    
# Exemplo de uso
obj = Subclasse()
print(obj.metodo_abstrato())  # Saída: Implementação do método abstrato na subclasse
print(Subclasse.metodo_estatico())  # Saída: Implementação do método estático na subclasse
print(Subclasse.metodo_de_classe())  # Saída: Implementação do método de classe na subclasse Subclasse
# A classe `Subclasse` implementa a classe abstrata `ClasseAbstrata`, fornecendo implementações concretas para os métodos abstratos definidos na classe base. Isso demonstra como as classes abstratas podem ser usadas para garantir que certas funcionalidades sejam implementadas, promovendo a consistência e a reutilização de código em diferentes subclasses.
# Classes abstratas são especialmente úteis em cenários onde você deseja definir um contrato comum para um grupo de subclasses, permitindo que essas subclasses implementem métodos específicos de acordo com suas necessidades. Isso é fundamental para a criação de sistemas flexíveis e extensíveis, onde novas funcionalidades podem ser adicionadas sem modificar o código existente.