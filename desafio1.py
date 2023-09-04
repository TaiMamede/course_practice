#Desafio:

#Recebe um valor inteiro, positivo, maior que zero.
#Guarde esse valor em uma variável chamada: numero.
#Receba uma frase, e guarde essa frase na variavel: texto
#Converta o numero recebido para Decimal(float) e guarde esse nova valor convertido na variável chamada x.
#Coloque todos os caracteres da frase recebida em maiúscula. e guarde na mesma variável texto.
#Imprima as duas variáveis: texto e x.

#Let's go!

numero = int(input("Digite um valor: "))
texto = str(input("Digite uma frase: "))
x = float(numero)
texto = texto.upper()
print(texto, x)

