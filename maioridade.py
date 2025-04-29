from datetime import datetime

menores = 0
maiores = 0
ano_atual = datetime.now().year

for c in range(7):  
    ano = int(input('Digite o ano que você nasceu: ')) 
    idade = ano_atual - ano 
 
    if idade >= 18:
        maiores += 1  
    else:
        menores += 1  
print(f'A quantidade de maiores é {maiores}')    
print(f'A quantidade de menores é {menores}')


 
