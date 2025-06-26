# Manipulação de arquivo CSV em Python é uma tarefa comum que envolve a leitura e escrita de dados em arquivos no formato CSV (Comma-Separated Values). Python fornece uma biblioteca chamada `csv` que facilita essa manipulação. Abaixo estão alguns exemplos básicos de como trabalhar com arquivos CSV em Python.
import csv
import os
# Verificando se o arquivo CSV existe
if os.path.exists("dados.csv"):
    # Abrindo o arquivo CSV em modo de leitura
    with open("dados.csv", "r", newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        # Lendo o conteúdo do arquivo CSV
        for linha in leitor_csv:
            print(linha)
else:
    print("O arquivo 'dados.csv' não existe.")
# Escrevendo no arquivo CSV
# Abrindo o arquivo CSV em modo de escrita (isso cria o arquivo se ele não existir
with open("dados.csv", "w", newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    # Escrevendo algumas linhas no arquivo CSV
    escritor_csv.writerow(["Nome", "Idade", "Cidade"])
    escritor_csv.writerow(["Alice", 30, "Nova York"])
    escritor_csv.writerow(["Bob", 25, "Los Angeles"])
    escritor_csv.writerow(["Charlie", 35, "Chicago"])
# Lendo o arquivo novamente para verificar o conteúdo
with open("dados.csv", "r", newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    print("Conteúdo do arquivo após escrita:")
    for linha in leitor_csv:
        print(linha)
# Adicionando mais conteúdo ao arquivo CSV
# Abrindo o arquivo CSV em modo de adição (isso não apaga o conteúdo existente
with open("dados.csv", "a", newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    # Adicionando mais linhas ao arquivo CSV
    escritor_csv.writerow(["David", 28, "Miami"])
    escritor_csv.writerow(["Eva", 22, "Seattle"])
# Lendo o arquivo novamente para verificar o conteúdo atualizado
with open("dados.csv", "r", newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    print("Conteúdo do arquivo após adição:")
    for linha in leitor_csv:
        print(linha)
# Removendo o arquivo CSV
# Se você quiser remover o arquivo após a manipulação, pode usar o seguinte código:
if os.path.exists("dados.csv"):
    os.remove("dados.csv")
    print("Arquivo 'dados.csv' removido com sucesso.")
else:
    print("O arquivo 'dados.csv' não existe para ser removido.")
# Este exemplo demonstra como manipular arquivos CSV em Python, incluindo leitura, escrita, adição de conteúdo e remoção do arquivo. A biblioteca `csv` é usada para facilitar a leitura e escrita de dados no formato CSV.
# A função `csv.reader` é usada para ler o conteúdo do arquivo CSV, enquanto `csv.writer` é usada para escrever dados no arquivo. O parâmetro `newline=''` é importante para evitar problemas de formatação em diferentes sistemas operacionais.
# O bloco `with` garante que o arquivo seja fechado corretamente após a manipulação. A função `os.path.exists` é usada para verificar se o arquivo existe antes de tentar abri-lo ou removê-lo, evitando erros. A função `os.remove` é usada para excluir o arquivo quando não é mais necessário. Esses métodos são fundamentais para a manipulação de arquivos CSV em Python e são amplamente utilizados em diversas aplicações.
# A manipulação de arquivos CSV é uma habilidade essencial em Python, especialmente para trabalhar com dados tabulares, como aqueles encontrados em planilhas e bancos de dados. A biblioteca `csv` oferece uma maneira eficiente e fácil de lidar com esses arquivos, permitindo que você leia, escreva e modifique dados de forma simples e intuitiva.
# Além disso, a manipulação de arquivos CSV é amplamente utilizada em ciência de dados, análise de dados e desenvolvimento de aplicativos, tornando essa habilidade valiosa para programadores e analistas. Com a capacidade de ler e escrever arquivos CSV, você pode facilmente importar e exportar dados entre diferentes sistemas e formatos, facilitando a integração de dados em suas aplicações.