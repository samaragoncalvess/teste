n = 0
for c in range(3, 500, 9):
    if c % 2 != 0:  
        n += c
print(f'A soma de todos os números ímpares, múltiplos de 3 é igual a {n}')
