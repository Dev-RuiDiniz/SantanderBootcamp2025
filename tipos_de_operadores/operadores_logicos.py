# Operadores Logicos são usados para combinar expressões booleanas.

valor = 10 
valor2 = 20

# Operador AND
resultado_and = (valor > 5) and (valor2 < 30)
print(f"Resultado do AND: {resultado_and}")  # True, pois ambas as condições são verdadeiras

# Operador OR
resultado_or = (valor < 5) or (valor2 < 30)
print(f"Resultado do OR: {resultado_or}")  # True, pois pelo menos uma condição é verdadeira

# Operador NOT
resultado_not = not (valor > 5)
print(f"Resultado do NOT: {resultado_not}")  # False, pois a condição é verdadeira e o NOT inverte o resultado

# Operador XOR (exclusivo)
resultado_xor = (valor > 5) ^ (valor2 < 30)
print(f"Resultado do XOR: {resultado_xor}")  # False, pois ambas as condições são verdadeiras, XOR é verdadeiro apenas se uma for verdadeira

