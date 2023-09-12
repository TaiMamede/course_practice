#Dado um numero inteiro qualquer, verificar se ele é:
#Positivo
#Par ou impar
#Apresentar a mensagem
#Testas condições
#abs (valor absoluto)

n = int(input("Entre com um número: "))

if (n >= 0):
    if(n % 2) == 0:
        (print(n, "é par positivo"))
    else:
        print(n, "é ímpar positivo!")
else:
    if(abs(n) % 2) == 0:
        print(n, "é par negativo!")
    else:
        print(n, "é impar negativo!")

