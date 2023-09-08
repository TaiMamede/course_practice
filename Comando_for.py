#Estrutura de Repetição
#Comando for
    #for <variável de interação> in <sequencia>:
        #comando(S)

#<sequencial>
#range ([inicio,] fim [,passo])

#ex:
#range(3) >>> 0, 1, 2
#range(2,6) >>> 2, 3, 4, 5
#range(2,7,2) >>> 2, 4, 6)

#Além de utlizar range... poderiamos utilizar uma "string"...
#Exemplo: Calculo do Fatorial de um numero

#Fatorial de n = 1*2*3*...*3
#Fatorial de 5 = 1*2*3*4*5 = 1*2=2 2*3=6 6*4=24 24*5=120 => 5! = 120
#Fatorial de 7 = 1*2*3*4*5*6*7 = 120*6=720 720*7= 5040   => 7! = 5040

numero = int(input("Entre com um numero inteiro positivo: "))
fatorial = 1
if numero < 0:
    print ("Fatorial nao existe!")
elif numero == 0:
    print("Fatorial de 0 é igual a 1")
else:
    for i in range(1, numero+1):
        fatorial = fatorial*i
    print (f"Fatorial de {numero} é igual a: {fatorial}")

