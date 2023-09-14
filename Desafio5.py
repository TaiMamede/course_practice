"""
Desafio: Faça um programa que recebe um numero (por exemplo: 12345).
Voce deve calcular e mostrar a soma dos digitos desse numero.
ex: 1+2+3+4+5 = 15
Faça isso utilizando o comando for ou while.
"""

number = int(input("number: "))
soma = 0
n = 0
while number != 0:
    n = number % 10
    soma += n
    number = int(number/10)

print(f"The sum of the digits: {soma}")



