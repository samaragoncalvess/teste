print('\033[0;33;41m.............TABUADA.............\033[m')
num = int(input("Escolha o seu número: "))
for c in range(1, 11):
    print(f'{num} x {c}= {num * c}')
