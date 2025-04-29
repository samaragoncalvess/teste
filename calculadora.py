n1 = float(input("Digite o valor 1:\n"))
operacao = input("Digite a operação que você deseja (+, *, -, /):\n")
n2 = float(input("Digite o valor 2:\n"))

if operacao == '+':
    resultado = n1 + n2
    print(f"O valor da soma é: {resultado:.2f}")
elif operacao == '*':
    resultado = n1 * n2
    print(f"O resultado da multiplicação é: {resultado:.2f}")
elif operacao == '-':
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado:.2f}")
elif operacao == '/':
    if n2 == 0:
        print("Erro! Divisão por zero.")  # Corrigi a indentação aqui
    else:
        resultado = n1 / n2
        print(f"O resultado da divisão é: {resultado:.2f}")  # Corrigi a indentação aqui
else:
    print("Operação inválida!")
