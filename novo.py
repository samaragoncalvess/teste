import random
al1=str(input('aluno 1'))
al2=str(input('aluno 2'))
al3=str(input('aluno 3'))
al4=str(input('aluno 4'))
alunos=(al1,al2,al3,al4)
sorteio=random.choice(alunos)
print(f'o aluno escolhido foi{sorteio}')

