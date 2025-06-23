# Args e Kwargs são formas de passar argumentos para funções em Python, permitindo maior flexibilidade. Args permite passar um número variável de argumentos posicionais, enquanto kwargs permite passar um número variável de argumentos nomeados. Isso é útil quando não se sabe quantos argumentos serão necessários ou quando se deseja passar opções adicionais.

def funcoes_args_kwargs():
    # Exemplo de uso de *args
    def soma_todos(*args):
        return sum(args)

    # Chamando a função com múltiplos argumentos
    resultado = soma_todos(1, 2, 3, 4, 5)
    print(f"A soma de todos os números é: {resultado}")

    # Exemplo de uso de **kwargs
    def exibir_informacoes(**kwargs):
        for chave, valor in kwargs.items():
            print(f"{chave}: {valor}")

    # Chamando a função com argumentos nomeados
    exibir_informacoes(nome="Maria", idade=30, cidade="São Paulo")

# Chamada da função de args e kwargs
funcoes_args_kwargs()

# Funções recursivas são aquelas que se chamam dentro de si mesmas, permitindo resolver problemas complexos de forma elegante. Elas são úteis para tarefas como calcular fatorial, Fibonacci e percorrer estruturas de dados como árvores.
def funcoes_recursivas():
    # Exemplo de função recursiva para calcular o fatorial de um número
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)

    # Chamando a função recursiva
    numero = 5
    resultado_fatorial = fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado_fatorial}")
# Chamada da função de recursão
funcoes_recursivas()

# Funções de ordem superior são aquelas que podem receber outras funções como argumentos ou retornar uma função. Elas são úteis para criar abstrações e manipular comportamentos de forma flexível.
def funcoes_ordem_superior():
    # Exemplo de função de ordem superior que recebe outra função como argumento
    def aplicar_funcao(funcao, valor):
        return funcao(valor)

    # Definindo uma função simples para ser passada como argumento
    def quadrado(x):
        return x ** 2

    # Chamando a função de ordem superior
    resultado = aplicar_funcao(quadrado, 5)
    print(f"O quadrado de 5 é: {resultado}")
# Chamada da função de ordem superior
funcoes_ordem_superior()

# Funções geradoras são aquelas que utilizam a palavra-chave `yield` para retornar valores de forma iterativa, permitindo economizar memória e criar sequências infinitas. Elas são úteis para gerar grandes conjuntos de dados ou fluxos contínuos de informações.
def funcoes_geradoras():
    # Exemplo de função geradora que produz uma sequência de números
    def contador(maximo):
        contador = 0
        while contador < maximo:
            yield contador
            contador += 1

    # Chamando a função geradora
    for numero in contador(5):
        print(f"Número gerado: {numero}")
# Chamada da função geradora
funcoes_geradoras()

# Funções decoradoras são aquelas que permitem modificar o comportamento de outras funções, adicionando funcionalidades extras sem alterar o código original. Elas são úteis para implementar padrões como logging, autenticação e cache.
def funcoes_decoradoras():
    # Exemplo de função decoradora que adiciona um comportamento extra
    def decorador(funcao):
        def funcao_decorada(*args, **kwargs):
            print("Antes da execução da função")
            resultado = funcao(*args, **kwargs)
            print("Após a execução da função")
            return resultado
        return funcao_decorada

    # Definindo uma função simples para ser decorada
    @decorador
    def saudacao(nome):
        return f"Olá, {nome}!"

    # Chamando a função decorada
    mensagem = saudacao("João")
    print(mensagem)
# Chamada da função decoradora
funcoes_decoradoras()

# Funções lambda são funções anônimas que podem ser definidas em uma única linha, geralmente usadas para operações simples e rápidas. Elas são úteis para criar funções pequenas e descartáveis, especialmente em contextos como mapeamento e filtragem de listas.
def funcoes_lambda():
    # Exemplo de função lambda para calcular o quadrado de um número
    quadrado = lambda x: x ** 2

    # Chamando a função lambda
    resultado_quadrado = quadrado(4)
    print(f"O quadrado de 4 é: {resultado_quadrado}")

    # Exemplo de uso de função lambda com map
    numeros = [1, 2, 3, 4, 5]
    quadrados = list(map(lambda x: x ** 2, numeros))
    print(f"Quadrados dos números: {quadrados}")
# Chamada da função lambda
funcoes_lambda()

# Funções de manipulação de strings são aquelas que permitem realizar operações comuns em textos, como conversão de maiúsculas/minúsculas, substituição de caracteres e divisão de strings. Elas são essenciais para trabalhar com dados textuais em Python.
def funcoes_manipulacao_strings():
    # Exemplo de manipulação de strings
    texto = "Python é uma linguagem de programação poderosa."

    # Convertendo para maiúsculas
    texto_maiusculo = texto.upper()
    print(f"Texto em maiúsculas: {texto_maiusculo}")

    # Convertendo para minúsculas
    texto_minusculo = texto.lower()
    print(f"Texto em minúsculas: {texto_minusculo}")

    # Substituindo uma palavra
    texto_substituido = texto.replace("poderosa", "incrível")
    print(f"Texto após substituição: {texto_substituido}")

    # Dividindo a string em palavras
    palavras = texto.split()
    print(f"Palavras no texto: {palavras}") 
# Chamada da função de manipulação de strings
funcoes_manipulacao_strings()

# Funções de manipulação de listas são aquelas que permitem realizar operações comuns em listas, como ordenação, filtragem e transformação de elementos. Elas são essenciais para trabalhar com coleções de dados em Python.
def funcoes_manipulacao_listas():
    # Exemplo de manipulação de listas
    numeros = [5, 2, 9, 1, 5, 6]

    # Ordenando a lista
    numeros_ordenados = sorted(numeros)
    print(f"Números ordenados: {numeros_ordenados}")

    # Filtrando números maiores que 5
    numeros_maiores_que_cinco = list(filter(lambda x: x > 5, numeros))
    print(f"Números maiores que 5: {numeros_maiores_que_cinco}")

    # Transformando a lista para o dobro dos valores
    numeros_dobrados = list(map(lambda x: x * 2, numeros))
    print(f"Números dobrados: {numeros_dobrados}")
# Chamada da função de manipulação de listas
funcoes_manipulacao_listas()

# Funções de manipulação de dicionários são aquelas que permitem realizar operações comuns em dicionários, como adição, remoção e atualização de chaves e valores. Elas são essenciais para trabalhar com dados estruturados em Python.
def funcoes_manipulacao_dicionarios():
    # Exemplo de manipulação de dicionários
    pessoa = {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo"
    }

    # Adicionando uma nova chave
    pessoa["profissao"] = "Desenvolvedor"
    print(f"Após adição: {pessoa}")

    # Removendo uma chave
    del pessoa["idade"]
    print(f"Após remoção: {pessoa}")

    # Atualizando um valor
    pessoa["cidade"] = "Rio de Janeiro"
    print(f"Após atualização: {pessoa}")

# Chamada da função de manipulação de dicionários
funcoes_manipulacao_dicionarios()

# Funções de manipulação de conjuntos são aquelas que permitem realizar operações comuns em conjuntos, como união, interseção e diferença. Elas são essenciais para trabalhar com coleções de dados únicos em Python.
def funcoes_manipulacao_conjuntos():
    # Exemplo de manipulação de conjuntos
    conjunto_a = {1, 2, 3, 4, 5}
    conjunto_b = {4, 5, 6, 7, 8}

    # União dos conjuntos
    uniao = conjunto_a.union(conjunto_b)
    print(f"União: {uniao}")

    # Interseção dos conjuntos
    intersecao = conjunto_a.intersection(conjunto_b)
    print(f"Interseção: {intersecao}")

    # Diferença dos conjuntos
    diferenca = conjunto_a.difference(conjunto_b)
    print(f"Diferença: {diferenca}")
# Chamada da função de manipulação de conjuntos
funcoes_manipulacao_conjuntos()

# Funções de manipulação de arquivos são aquelas que permitem realizar operações comuns em arquivos, como leitura, escrita e fechamento. Elas são essenciais para trabalhar com dados persistentes em Python.
def funcoes_manipulacao_arquivos():
    # Exemplo de manipulação de arquivos
    # Criando e escrevendo em um arquivo
    with open("exemplo.txt", "w") as arquivo:
        arquivo.write("Olá, mundo!\n")
        arquivo.write("Este é um exemplo de manipulação de arquivos em Python.")

    # Lendo o conteúdo do arquivo
    with open("exemplo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(f"Conteúdo do arquivo:\n{conteudo}")
# Chamada da função de manipulação de arquivos
funcoes_manipulacao_arquivos()
