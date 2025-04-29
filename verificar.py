senha = input("Digite sua senha (somente letras minúsculas): ")

if senha.isupper():  # Verifica se está em maiúsculas
    print("Erro: Sua senha está em maiúsculas. Somente letras minúsculas são aceitas!")
else:
    print("Senha aceita!")
