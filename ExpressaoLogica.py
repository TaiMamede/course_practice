# Diferentemente de uma expressão matemática onde um resultado pode ser um número, ou uma variável,
# ou uma combinação de variável, uma expressão lógica sempre resulta em dois valores possíveis:
# VERDADEIRO (True) ou FALSO (False)

#Ex.:
x = 3
y = 5
z = x > y
print(z)

r = y >= x
print(r)

#Operadores Relacionais

# a=10 , b=20
# == (igual): a==b = False
# != (diferente): a!=b = True
# > (maior que): a>b = False
# < (menor que): a<b = True
# >= (maior ou igual): a>=b = False
# <= (menor ou igual): a<=b = True

#Operadores Logicos (Tabela verdade)

# and (é logico) a and b: False
# or (ou logico) a or b: True
# not (não logico) not a: False

p = 5
q = 7
a = (p > q) and (not(p == q))
print(a)
b = (not(q<p)) or (q != p)
print(b)

#Prioridades em Python:

#() Parenteses
#** Exponente
#+x, -x soma ou subtração unária
#*,/,//,% multiplicação, divisão, divisão inteira e módulo
#+,- adição e subtração
#==, !=, >, >=, <, <= operadores de comparação
#not, and, or


