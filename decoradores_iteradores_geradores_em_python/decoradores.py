# Decoradores em Python são funções que permitem modificar o comportamento de outras funções ou métodos.
# Eles são frequentemente usados para adicionar funcionalidades, como autenticação, logging, ou medição de desempenho.

def decorador(funcao):
    """
    Decorador que imprime uma mensagem antes e depois da execução da função decorada.
    """
    def funcao_decorada(*args, **kwargs):
        print("Antes de chamar a função.")
        resultado = funcao(*args, **kwargs)
        print("Depois de chamar a função.")
        return resultado
    return funcao_decorada

@decorador
def minha_funcao(nome):
    """
    Função de exemplo que recebe um nome e retorna uma saudação.
    """
    return f"Olá, {nome}!"
# Exemplo de uso do decorador
if __name__ == "__main__":
    print(minha_funcao("Maria"))
# Neste exemplo, o decorador `decorador` é aplicado à função `minha_funcao`.
# Quando `minha_funcao` é chamada, o decorador executa código antes e depois da chamada da função original,
# imprimindo mensagens no console. O resultado da função original é retornado normalmente.
# Decoradores são uma maneira poderosa de modificar o comportamento de funções sem alterar seu código.