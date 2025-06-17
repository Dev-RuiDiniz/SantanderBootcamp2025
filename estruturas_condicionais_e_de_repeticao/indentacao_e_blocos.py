# Indentação e blocos são fundamentais em Python para definir a estrutura do código.
# A indentação correta é crucial para o funcionamento do código, pois define blocos de código
# que pertencem a estruturas condicionais, loops e funções.

# Exemplo de indentação correta:
if True:
    print("Este bloco está indentado corretamente.")
    if False:
        print("Este bloco também está indentado corretamente.")
        
# Exemplo de indentação incorreta:
#if True:
#print("Este bloco não está indentado corretamente.")
# Isso causará um erro de sintaxe, pois o Python espera que o código dentro do bloco `if` esteja indentado

# Exemplo de uso de blocos com loops e condicionais
for i in range(3):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")