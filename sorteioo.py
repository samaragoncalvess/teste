import random

alunos = [] 

for _ in range(4):  
    nome = str(input('Digite o seu nome: '))
    alunos.append(nome)  # Adiciona o nome à lista
    

sorteio = random.choice(alunos)
print(f'O aluno escolhido foi {sorteio}')

