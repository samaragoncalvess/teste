velocidade=float(input('qual a velocidade do carro?'))
if velocidade <= 80:
    print('\033[1;31;47mtenha um bom dia, diriga com segurança')
else:
    print('Você foi multado! ultrapassou o limite de 80k/h')
    multa=velocidade*7
    print (f'você deve pagar uma multa de \033[31m{multa:.1f} R$')
    

