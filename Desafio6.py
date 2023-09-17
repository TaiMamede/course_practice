"""
Desafio:
Fazer um programa em python que:
-Receba as informações (nome, idade e n. do calçado) de 5 pessoas
-Depois de receber as informações você deve mostrar a relação completa das pessoas e duas informações, em ordem
alfabética de nome).
-Ao final do relatório, você deve calcular e mostrar as seguintes informações: -a média de idades das pessoas e
-número médio dos calçados das pessoas pesquizadas.
"""
dados = []
for i in range(1,6):
    print(f"Pessoa{i}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    n_do_calcado = int(input("Numero do calçado: "))
    print("-------------------------------------------")
    pessoa = [nome, idade, n_do_calcado]
    dados.append(pessoa)


#Criar uma nova lista ordenada a partir da lista "dados"
new_list_dados = sorted(dados)

#Mostrar lista e as medias
total_idades = 0
total_calcados = 0

for i in range(0,5):
    total_idades += new_list_dados[i][1]
    total_calcados += new_list_dados[i][2]
    print(f"{new_list_dados[i][0]} - {new_list_dados[i][1]} - {new_list_dados[i][2]}")

print("----------------------------------------------------------------------")
print(f"Media das Idades: {total_idades/5}")
print(f"Media dos numeros de calçados: {total_calcados/5}")







