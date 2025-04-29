numero = int(input('Digite um número: '))

print('Escolha uma base para conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')

escolha = int(input('Qual a sua escolha? '))

if escolha == 1:
    print(f'O número \033[0;30;41m{numero} em binário é: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O número {numero} em octal é: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'0 número {numero} em hexadecimal é: {hex(numero)[2:]}')
else:
    print('Opção inválida! Por favor, escolha 1, 2 ou 3.')

