sexo=str(input(' digite o seu sexo, (m/f):')).strip().lower()
while sexo not in ('m', 'f'):
    sexo=str(input('voce digitou errado, digite novamente')).strip().lower()
print (f'sexo {sexo} registrado com sucesso')     