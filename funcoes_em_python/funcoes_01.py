# Funções em Python são blocos de código reutilizáveis que realizam uma tarefa específica. Elas podem receber parâmetros, executar operações e retornar valores. As funções ajudam a organizar o código, tornando-o mais legível e modular.

def funcoes_basicas():
    # Definindo uma função simples que recebe um parâmetro e retorna um valor
    def saudacao(nome):
        return f"Olá, {nome}!"

    # Chamando a função com um argumento
    mensagem = saudacao("Maria")
    print(mensagem)

    # Definindo uma função com múltiplos parâmetros
    def soma(a, b):
        return a + b

    # Chamando a função de soma
    resultado = soma(5, 3)
    print(f"A soma de 5 e 3 é: {resultado}")

    # Definindo uma função com valor padrão para um parâmetro
    def saudacao_personalizada(nome, saudacao="Olá"):
        return f"{saudacao}, {nome}!"

    # Chamando a função com e sem o parâmetro padrão
    print(saudacao_personalizada("João"))
    print(saudacao_personalizada("Ana", "Bom dia"))

    # Definindo uma função que retorna múltiplos valores
    def operacoes(a, b):
        soma = a + b
        subtracao = a - b
        return soma, subtracao

    # Chamando a função e desempacotando os valores retornados
    resultado_soma, resultado_subtracao = operacoes(5, 3)
    print(f"A soma de 5 e 3 é: {resultado_soma}")
    print(f"A subtração de 5 e 3 é: {resultado_subtracao}")
    
    # Definindo uma função anônima (lambda) para calcular o quadrado de um número
    quadrado = lambda x: x ** 2
    # Chamando a função lambda
    resultado_quadrado = quadrado(4)
    print(f"O quadrado de 4 é: {resultado_quadrado}")
    