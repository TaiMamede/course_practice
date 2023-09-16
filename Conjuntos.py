"""
Fazer um programa em python que:
-Receba uma quantidade variavel de strings (termine a digitação com string vazia = '')
-Guarde essa informação em uma lista
-Crie uma outra lista onde cada elemento se transformará em uma lista de carcteres únicos (não repetidos).Ex:
se uma palavra da lista for igual a : 'barbante', você a modificará par: ['b', 'a', 'r', 'n', 't', 'e'] sem repetições
-Em seguida mostre a lista modificada
"""

palavras = []
lista = []

while True:
    palavra = input("palavra: ")
    if palavra == '':
        break
    else:
        palavras.append(palavra)

for palavra in palavras:
    lista.append(list(set(palavra)))

for item in lista:
    print(item)