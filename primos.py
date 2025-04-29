num = int(input('Digite o número: '))
tot = 0  # Inicializando a variável tot

for a in range(1, num + 1):
    if num % a == 0:  # Se for divisor
        print('\033[31m', end='')  # Vermelho para divisores
        tot += 1
    else:
        print('\033[33m', end='')  # Amarelo para não divisores
    print(f'{a}', end=' ')  # Mostra o número

print(f'\nO número {num} foi divisível {tot} vezes.')

if tot == 2:  # Se for divisível apenas por 1 e por ele mesmo
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')


