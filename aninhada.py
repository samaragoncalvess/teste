nome = str(input('Qual o seu nome?')).strip()  # Remove espaços extras antes e depois
if nome == 'Samara':
    print('Que nome lindo você tem')
elif nome in ['Pedro', 'Gustavo', 'Felipe', 'Joana', 'Maria']:
    print('Seu nome é bem popular no Brasil')
elif nome in ['Ana', 'Laura', 'Ester', 'Beatriz', 'Elisa', 'Aylla']:
    print('Esse nome feminino é lindo')
else:
    print('Seu nome é bem normal')
    print(f'Tenha um bom dia, {nome}')

