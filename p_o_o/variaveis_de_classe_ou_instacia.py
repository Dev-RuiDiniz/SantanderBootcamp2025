# Variaveis de classe ou de instância
# As variáveis de classe são compartilhadas entre todas as instâncias da classe, enquanto as variáveis de instância são específicas para cada objeto.

class ContaBancaria:
    taxa_juros = 0.05  # variável de classe

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial  # variável de instância

    def aplicar_juros(self):
        self.saldo += self.saldo * ContaBancaria.taxa_juros

# Exemplo de uso
conta1 = ContaBancaria(1000)
conta2 = ContaBancaria(2000)
conta1.aplicar_juros()
conta2.aplicar_juros()
print(f"Saldo da conta 1 após aplicar juros: {conta1.saldo}")
print(f"Saldo da conta 2 após aplicar juros: {conta2.saldo}")

# Alterando a variável de classe
ContaBancaria.taxa_juros = 0.07
conta1.aplicar_juros()
print(f"Saldo da conta 1 após alterar a taxa de juros: {conta1.saldo}")
print(f"Saldo da conta 2 após alterar a taxa de juros: {conta2.saldo}")

# A variável de classe `taxa_juros` é compartilhada entre todas as instâncias da classe `ContaBancaria`.
# As variáveis de instância `saldo` são específicas para cada objeto, permitindo que cada conta tenha seu próprio saldo independente das outras.
# Isso demonstra como as variáveis de classe e de instância funcionam em Python, permitindo a criação de classes mais flexíveis e reutilizáveis.