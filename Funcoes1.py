"""
PARAMETRO/ARGUMENTO: Variável de entrada recebida pela função
RETORNO: Variável de saída da função
"""


# escrevendo uma função sem parametros de entrada e sem retorno
def funcao():
    #codigo

# chamar função
funcao()

# escrevendo uma função com parâmetro
'''OBS: Notação com definição do tipo do parâmetro de entrada e retorno'''
def funcao_com_parametro(parametro: int) -> None:
    print(parametro)

# escrevendo uma função com parâmetro NAO OBRIGATÓRIO
def funcao_sem_parametro_obrigatorio(parametro=None):
    pass

# chamar função com parâmetro
funcao_com_parametro('parametro')
funcao_com_parametro('variavel')
funcao_sem_parametro_obrigatorio()

# escrevendo uma função com retorno
def funcao():
    return retorno

# chamar função com retorno
retorno = funcao()


# escrevendo uma função com retorno
def funcao():
    return retorno

# chamar função com retorno
retorno = funcao()