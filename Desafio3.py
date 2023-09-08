#Desafio:
#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo
#que calcule seu peso ideal, utilizando as seguintes fórmulas:
    #Para homens: (72.7*h) - 58;
    #Para mulheres: (62.1*h) - 44,7.

#Let's go!

altura = float(input("Digite sua altura: "))
genero = (input("Qual o seu sexo <F ou >M: "))

if (genero == "M"):
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.
print("Seu peso ideal é ", peso)





