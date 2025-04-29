soma = 0
for n in range(6):
    try:
        n = int(input('Digite os números: '))
        if n % 2 == 0:
            soma += n
    except ValueError:
        print("Por favor, insira um número válido.")
print(f'A soma de todos os valores é: {soma}')
