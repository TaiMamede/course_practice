#Practice
#Resolução com elif( nota >=0.9 = A, nota >=0.8 = B, nota >=0.7 = C, nota >= 0.6 D, <0.6 = F)

nota = float(input("Nota: "))
if (nota<0) or (nota>1):
    print("Entrada errada!")
elif nota >= 0.9:
    print("Conceito A")
elif nota >= 0.8:
    print("Conceito B")
elif nota >= 0.7:
    print("Conceito C")
elif nota >= 0.6:
    print("Conceito D")
else:
    print("Conceito F")

#Another ex.:

#Banana: 5,23 / Maça: 12,10 / Cereja: 58,00

fruta = input("Fruta:")
if (fruta == "Banana"):
    print("O quilo da Banana é 5,23 reais")
elif (fruta == "Maça"):
    print("O quilo da Maça é 12,10 reais")
elif (fruta == "Cereja"):
    print("O quilo da Cereja é 58,00 reais")
else:
    print("Desculpe nao temos", fruta)

