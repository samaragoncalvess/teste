for _ in range(10):  # Limita a 10 tentativas, por exemplo
    senha = input("Digite sua senha (somente letras minúsculas): ")

    if senha.isupper():  # Verifica se está em maiúsculas
        print("Erro: Sua senha está em maiúsculas. Somente letras minúsculas são aceitas!")
    else:
        print("Senha aceita!")
        break  # Sai do loop ao acertar
else:
    print("Você excedeu o número de tentativas.")
