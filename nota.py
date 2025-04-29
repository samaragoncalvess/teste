n1=float(input('Digite n1')) 
n2=float(input('digite n2'))
media=n1+n2/2
print(f'A sua media foi {media},')
if media < 5:
    print('você foi reprovado')
elif media == 5 or  media <=6.9:
    print('Você esta de recuperaçao')
elif media >=7:
    print(' você foi aprovado') 

