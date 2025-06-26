# Arquivo TXT
# Manipulação de arquivos TXT em Python é uma tarefa comum que envolve a leitura e escrita de dados em arquivos de texto. Python fornece uma interface simples e intuitiva para trabalhar com arquivos TXT, permitindo que você abra, leia, escreva e feche arquivos facilmente. Abaixo estão alguns exemplos básicos de como manipular arquivos TXT em Python.
# Importando o módulo necessário
import os
# Verificando se o arquivo existe
if os.path.exists("arquivo.txt"):
    # Abrindo o arquivo em modo de leitura
    with open("arquivo.txt", "r") as arquivo:
        # Lendo o conteúdo do arquivo
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
else:
    print("O arquivo 'arquivo.txt' não existe.")
# Escrevendo no arquivo
# Abrindo o arquivo em modo de escrita (isso cria o arquivo se ele não existir)
with open("arquivo.txt", "w") as arquivo:
    # Escrevendo algumas linhas no arquivo
    arquivo.write("Esta é a primeira linha.\n")
    arquivo.write("Esta é a segunda linha.\n")
    arquivo.write("Esta é a terceira linha.\n")
# Lendo o arquivo novamente para verificar o conteúdo
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo após escrita:")
    print(conteudo)
# Adicionando mais conteúdo ao arquivo
# Abrindo o arquivo em modo de adição (isso não apaga o conteúdo existente) 
with open("arquivo.txt", "a") as arquivo:
    # Adicionando mais linhas ao arquivo
    arquivo.write("Esta é a quarta linha.\n")
    arquivo.write("Esta é a quinta linha.\n")
# Lendo o arquivo novamente para verificar o conteúdo atualizado
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo após adição:")
    print(conteudo)
# Removendo o arquivo
# Se você quiser remover o arquivo após a manipulação, pode usar o seguinte código:
if os.path.exists("arquivo.txt"):
    os.remove("arquivo.txt")
    print("Arquivo 'arquivo.txt' removido com sucesso.")
else:
    print("O arquivo 'arquivo.txt' não existe para ser removido.")
# Este exemplo demonstra como manipular arquivos TXT em Python, incluindo leitura, escrita, adição de conteúdo e remoção do arquivo. A função `open` é usada para abrir o arquivo em diferentes modos (`r` para leitura, `w` para escrita e `a` para adição), e o bloco `with` garante que o arquivo seja fechado corretamente após a manipulação.
# A função `os.path.exists` é usada para verificar se o arquivo existe antes de tentar abri-lo ou removê-lo, evitando erros. A função `os.remove` é usada para excluir o arquivo quando não é mais necessário. Esses métodos são fundamentais para a manipulação de arquivos em Python e são amplamente utilizados em diversas aplicações.