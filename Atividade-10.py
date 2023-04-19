print('''-----operação matematica:-----
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão''')
op = int(input('Digite aqui:'))
print()
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))


def calculadora(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        return num1 / num2
    else:
        return 0


res = calculadora(num1, num2, op)
print('Resultado', res)
