casa=float (input('Qual o valor da casa?'))
salario =float (input('qual o seu salario?'))
anos =int(input('Quantos anos quer pagar?'))
prestacao= casa/(anos*12)
minimo=salario*30/100
print (f'para pagar uma casa de {casa:.2f} em {anos} anos')
print ( f'a prestaçao será de {prestacao:.2f}')
if prestacao <=minimo:
    print ('seu emprestimo foi concedido')
else:
    print('seu emprestimo não pode ser concedido')

          
                