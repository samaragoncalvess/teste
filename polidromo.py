frase = input("Qual a frase? ").upper().replace(" ", "")
frase_invertida = frase[::-1]  # Inverte a frase

print(f"Frase original (sem espaços): {frase}")
print(f"Frase invertida: {frase_invertida}")

if frase == frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
