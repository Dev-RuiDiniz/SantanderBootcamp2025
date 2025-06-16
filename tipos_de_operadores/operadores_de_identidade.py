# Operadores de Identidade são usados para verificar se duas variáveis referenciam o mesmo objeto na memória.

variavel1 = [1, 2, 3]
variavel2 = variavel1  # variavel2 referencia o mesmo objeto que variavel1  

# Operador is
resultado_is = variavel1 is variavel2
print(f"Resultado do is: {resultado_is}")  # True, pois variavel2 é o mesmo objeto que variavel1

# Operador is not
resultado_is_not = variavel1 is not variavel2
print(f"Resultado do is not: {resultado_is_not}")  # False, pois variavel2 é o mesmo objeto que variavel1

# Criando uma nova lista para comparar
variavel3 = [1, 2, 3]  # variavel3 é um novo objeto com o mesmo conteúdo
resultado_is_novo = variavel1 is variavel3
print(f"Resultado do is com novo objeto: {resultado_is_novo}")  # False, pois variavel3 é um objeto diferente, apesar de ter o mesmo conteúdo

# Comparando com is not
resultado_is_not_novo = variavel1 is not variavel3
print(f"Resultado do is not com novo objeto: {resultado_is_not_novo}")  # True, pois variavel3 é um objeto diferente de variavel1

# Comparando com None
variavel4 = None
resultado_is_none = variavel4 is None
print(f"Resultado do is com None: {resultado_is_none}")  # True, pois variavel4 é None

resultado_is_not_none = variavel4 is not None
print(f"Resultado do is not com None: {resultado_is_not_none}")  # False, pois variavel4 é None
# Comparando com um objeto diferente de None
