# Metodos da lista em Python são funções que permitem manipular listas de diversas maneiras, como adicionar, remover, ordenar e inverter elementos. Esses métodos são essenciais para trabalhar com listas de forma eficiente e flexível.

# Exemplo de métodos de lista em Python
def metodos_list():
    # Criando uma lista de frutas
    frutas = ['maçã', 'banana', 'laranja', 'uva']
    
    # Adicionando um elemento ao final da lista
    frutas.append('kiwi')
    print("Após append:", frutas)
    
    # Inserindo um elemento em uma posição específica
    frutas.insert(2, 'abacaxi')
    print("Após insert:", frutas)
    
    # Removendo um elemento pelo valor
    frutas.remove('banana')
    print("Após remove:", frutas)
    
    # Removendo o último elemento da lista
    ultima_fruta = frutas.pop()
    print("Após pop (removido):", ultima_fruta)
    print("Lista após pop:", frutas)
    
    # Ordenando a lista
    frutas.sort()
    print("Após sort:", frutas)
    
    # Invertendo a ordem da lista
    frutas.reverse()
    print("Após reverse:", frutas)
    
    # Verificando o tamanho da lista
    tamanho = len(frutas)
    print("Tamanho da lista:", tamanho)
    
    # Verificando se um elemento está na lista
    existe = 'maçã' in frutas
    print("A maçã está na lista?", existe)
    
# Chamada da função de métodos de lista
metodos_list()