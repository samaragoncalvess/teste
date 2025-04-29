import unicodedata

# Função para remover acentos


def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize(
        'NFD', texto)  # Decomposição de caracteres
    texto_sem_acentos = ''.join(
        # Remove acentos
        c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sem_acentos

# Função para juntar a frase e remover espaços e acentos


def juntar_e_limpar(texto):
    texto_sem_espacos = texto.replace(" ", "")  # Remove espaços
    texto_limpo = remover_acentos(texto_sem_espacos)  # Remove acentos
    return texto_limpo.lower()  # Converte para minúsculas


# Entrada do usuário
frase = input("Digite uma frase: ")

# Limpa a frase (remove espaços, acentos e converte para minúsculas)
frase_limpa = juntar_e_limpar(frase)

print(f"Texto limpo: {frase_limpa}")
