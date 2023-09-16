"""
Fazer um programa em python que:
-Receba o cadastro de uma qtd ilimitada de proprietários e seus respectivos apartamentos
(numero do apartamento e nome do proprietário)
-Guarde essas informações em um dicionário, onde a chave de busca é o número do apto
-Para encerrar a digitação o número do apto será -1
-Em seguida, deve-se mostrar uma listagem em ordem crescente de apto: apto - nome proprietário
-No final apresente a quantidade total de apto listados
"""

proprietarios = {}

while True:
    apto = int(input("Digite o apto: "))
    if apto != -1:
        proprietario = input("Proprietário: ")
        proprietarios.update({apto:proprietario})
    else:
        break


edificio = dict(sorted(proprietarios.items()))

for chave, valor in edificio.items():
    print(f"{chave} - {valor}")

print(f"Total de aptos: {len(edificio)}")



