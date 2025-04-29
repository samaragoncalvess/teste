distancia=float(input('Qual a distancia da viagem?'))
print(f'Você esta prestes a comecar uma viagem de {distancia}km/h,')
if distancia <=200:
    preco1=distancia*0.50
    print(f'o preço da sua passagem é {preco1:.2f} R$')
else:
    preco2=distancia*0.45
    print(f'o preço da sua passagem é de {preco2:.2f} R$')