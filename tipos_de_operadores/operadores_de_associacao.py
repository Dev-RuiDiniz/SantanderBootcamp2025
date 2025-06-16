# Operadores de Associação são usados para verificar se dois objetos estão relacionados de alguma forma, como em uma estrutura de dados ou coleção.

valor1 = [1, 2, 3, 4, 5]
valor2 = 3

# Operador in
resultado_in = valor2 in valor1
print(f"Resultado do in: {resultado_in}")  # True, pois 3 está na lista valor1

# Operador not in
resultado_not_in = valor2 not in valor1
print(f"Resultado do not in: {resultado_not_in}")  # False, pois 3 está na lista valor1

# Verificando se um elemento não está na lista
valor3 = 6
resultado_not_in_2 = valor3 not in valor1
print(f"Resultado do not in com 6: {resultado_not_in_2}")  # True, pois 6 não está na lista valor1

# Verificando se uma chave está em um dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3}
resultado_in_dict = 'b' in dicionario
print(f"Resultado do in em dicionário: {resultado_in_dict}")  # True, pois 'b' é uma chave no dicionário

# Verificando se uma chave não está em um dicionário
resultado_not_in_dict = 'd' not in dicionario
print(f"Resultado do not in em dicionário: {resultado_not_in_dict}")  # True, pois 'd' não é uma chave no dicionário

# Verificando se um valor está em um dicionário
resultado_in_value = 2 in dicionario.values()
print(f"Resultado do in em valores de dicionário: {resultado_in_value}")  # True, pois 2 é um valor no dicionário

# Verificando se um valor não está em um dicionário
resultado_not_in_value = 4 not in dicionario.values()
print(f"Resultado do not in em valores de dicionário: {resultado_not_in_value}")  # True, pois 4 não é um valor no dicionário
