#Estrutura de Repetição
#Definida:

#Comando while

#while <expressão logica>:
#   comando

#O(s) comando(s) serão retidos ate que a expressão logica seja considerada false.

#Ex. Mostrar a tabuada do número 8

i = 1
while i < 11:
    print(i, "x 8 = ", i*8)
    i += 1

#Another ex.
#Receber valores do usuário (não se sabe quantos), até que a entrada for -1.
#E calcular a media de todosos valores digitados.

soma = 0
qtd = 0
numero = 0
while numero != -1:
    numero = int(input("Entre com um valor <-1 para sair>: "))
    if (numero != -1):
        soma += numero
        qtd += 1
media = soma /qtd
print("A media dos valores: ", media)

