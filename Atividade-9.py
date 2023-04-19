print('-------Usando for com range ()-------')
print()

for i in range(1, 21):
    if i == 13:
        continue
    print(i, 'º Andar')

print()
print('-------Usando while-------')
print()

i = 0
while i != 20:
    i = i + 1
    if i == 13:
        continue
    print(i, 'º Andar')

print()
print('-------Reverso-------')
print()

for i in range(20, 0, -1):
    if i == 13:
        continue
    print(i, 'º andar')
