# Quantidade de roda
rodas = int(input('Quantidade de rodas:'))
# Peso bruto em kg
peso = int(input('Peso bruto em KG:'))
# Quantidade de pessoas no veículo
pessoas = int(input('Quantidade de pessoas:'))

# Categoria A
if rodas <= 3:
    print('É um veículo da categoria A')
# Categoria B
elif rodas == 4 and pessoas <= 8 and peso <= 3500:
    print('É um veículo da categoria B')
# Categoria C
elif rodas >= 4 and 3501 >= peso <= 6000:
    print('É um veículo da categoria C')
# Categoria D
elif rodas >= 4 and pessoas >= 8:
    print('É um veículo da categoria D')
# Categoria E
elif rodas >= 4 and peso >= 6001:
    print('É um veículo de categoria E')
