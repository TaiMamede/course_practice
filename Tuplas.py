"""
Tuplas: fazer um programa em python que:
-receba uma quantidade ilimitada de idade de pessoas
-guarde essas idades em uma lista
-para encerrar a digitação das idades, deve-se digitar: -1
-em seguida, deve-se gerar uma tupla de idades, a partir da lista
-Deve se mostrar as seguintes informações, consultando a tupla: -Qtd de idades digitadas e -média das idades
"""

lista_idades = []
while True:
    idades = int(input("Idade: "))
    if idades != -1:
        lista_idades.append(idades)
    else:
        break

tupla_idades = tuple(lista_idades)

qtd = len(tupla_idades)
total = sum(tupla_idades)
media = total/qtd

print(f"Total de idades digitadas: {qtd}")
print(f"Media das idades: {media}")
