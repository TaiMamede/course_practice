resultado = []
while True:
    number = int(input("Digite o resultado: "))
    resultado.append(number)
    if number >= 100:
        print(f"Meta batita!{resultado}")
        soma = 0
        for i in resultado:
            soma += i
        print(f'Média é:{soma/len(resultado)}')
        break
    elif number == 0:
        print(f"Meta nao alcançada!{resultado}")
        break










