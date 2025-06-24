# Construtores e Destrutores são métodos especiais em Python que permitem inicializar e limpar objetos de forma controlada. O construtor é chamado automaticamente quando um objeto é criado, enquanto o destrutor é chamado quando o objeto é destruído.

class Exemplo:
    def __init__(self, valor):
        self.valor = valor
        print(f"Construtor chamado: {self.valor}")

    def __del__(self):
        print(f"Destrutor chamado: {self.valor}")

# Exemplo de uso:
objeto = Exemplo("Teste")
del objeto
# Saída esperada:
# Construtor chamado: Teste
# Destrutor chamado: Teste  
# Nota: O destrutor pode não ser chamado imediatamente após o uso do objeto, pois o coletor de lixo do Python gerencia a memória automaticamente.
# É importante lembrar que o uso de destrutores não é comum em Python, pois a linguagem possui um coletor de lixo que cuida da liberação de memória. No entanto, eles podem ser úteis em casos específicos, como liberar recursos externos (arquivos, conexões de rede, etc.) quando o objeto não é mais necessário.

