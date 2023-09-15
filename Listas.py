'''
Programa em python que: recebe uma quantidade ilimitada de nome de cidades em uma lista,
para encerrar a digitação deve-se digitar: "sair".
em seguida deve-se ordernar essa lista de cidades em ordem crescente,
e mostrar a relação das cidades ordenadas, 1 por linha.
'''
cidades = []

while True:
    cidade = input("Digite uma cidade: ")
    if cidade == "sair":
        break
    else:
        cidades.append(cidade)

if len(cidades) > 0:
        cidades.sort()

        for cidade in cidades:
            print(cidade)

else:
    print("A lista de cidade está vazia")




