#Estruturas de Repetição
#São estruturas (comandos) que dão mais movimento aos nossos programas/scripts
#Permite que uma determinada ação seja executada mais de uma vez sem que tenhamos que executar novamente o script
#Por exemplo: podemos testar entradas de dados e pedir que o usuário repita a entrada ate que um valor válido
#seja digitado.

#Ex.
#Programa para calcular a idade media de seus colegas

soma = 0
for i in range(1,6):
    idade = int(input("Entre com a idade: "))
    soma = soma + idade
media = soma/5
print("A media das idades são: ", media)

#Another ex.
#Usando while

soma = 0
i = 1
while i <= 5:
    idade = int(input("Entre com a idade: "))
    soma = soma + idade
    i = i + 1
media = soma/5
print("A media das idades são: ", media)