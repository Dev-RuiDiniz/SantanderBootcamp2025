# Interpolação de variáveis em strings é uma técnica que permite inserir valores de variáveis diretamente dentro de strings, facilitando a construção de mensagens dinâmicas. Em Python, isso pode ser feito de várias maneiras, incluindo o uso de f-strings (a partir do Python 3.6), o método `format()`, e a interpolação com o operador `%`.
# A forma mais moderna e recomendada é o uso de f-strings, que são strings literais prefixadas com `f` ou `F`, permitindo a inclusão de expressões dentro de chaves `{}`.

# Exemplo de uso de f-strings
def exemplo_f_strings(nome, idade):
    mensagem = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
    return mensagem

# Exemplo de uso do método format()
def exemplo_format(nome, idade):
    mensagem = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
    return mensagem

# Exemplo de uso da interpolação com o operador %
def exemplo_interpolacao(nome, idade):
    mensagem = "Olá, meu nome é %s e eu tenho %d anos." % (nome, idade)
    return mensagem

# Função principal para demonstrar os exemplos
def main():
    nome = "Alice"
    idade = 30
    
    print(exemplo_f_strings(nome, idade))
    print(exemplo_format(nome, idade))
    print(exemplo_interpolacao(nome, idade))
    
# Chamada da função principal
if __name__ == "__main__":
    main()