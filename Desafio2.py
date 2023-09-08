#Desafio:
# Fazer um programa em python que leia um numero inteiro, positivo,
# maior que zero e verifique se esse número é par ou ímpar

num = int(input("Número: "))
if (num >= 0):
    if (num % 2) == 0:
        print(num, "é um número par positivo!")
    else:
        print(num, "é um número impar positivo")

