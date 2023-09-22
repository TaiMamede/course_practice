"""
Testing functions - função sem parametro e com retorno
"""

def um_megabit():
    valor = pow(2, 20)
    return valor

#poderia fazer:
#def um_megabit():
#   return pow(2, 20)

x = um_megabit()
print(x)


