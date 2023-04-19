print('------- Calculadora -------')
print()

sair = 1
while sair != 0:
    print('''Selecione a operação:
( 1 ) Soma
( 2 ) Subtração
( 3 ) Multiplicação
( 4 ) Divisão
( 0 ) Sair''')
    op = int(input('Digite aqui:'))

    print('------------------------')
    # VERIFICAÇÃO SE O VALOR DA OPERACÃO ESTA CORRETA
    if 0 <= op <= 4:
        # VERIFICAÇÃO SE É 0 OU NÂO
        if op != 0:
            n1 = int(input('Digite um número:'))
            n2 = int(input('Digite outro número:'))

            # PROCESSAMENTO
            def Calculadora(n1, n2, op):
                # soma
                if op == 1:
                    res = n1 + n2
                    op = 'SOMA'
                # Subtração
                elif op == 2:
                    res = n1 - n2
                    op = 'SUBTRAÇÃO'
                # Multiplicação
                elif op == 3:
                    res = n1 * n2
                    op = 'MULTIPLICAÇÃO'
                # Divisão
                elif op == 4:
                    if n2 != 0:
                        res = n1 / n2
                        op = 'DIVISÃO'
                    else:
                        res = 0
                return res, op

            res, op = Calculadora(n1, n2, op)
            # RESULTADO
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'O resultado da {op} entre {n1} e {n2} é {res}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        else:
            sair = 0
            print('SAINDO...')
    else:
        print("Essa opção não existe")
        print('------------------------')