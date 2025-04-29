n1 = float(input("digite a sua primeira nota :"))
n2 = float(input("digite a sua segunda nota:"))
n3 = float(input("digite a sua terceira nota"))
media = (n1+n2+n3)/3
print(f' a sua media foi {media:.2f}')
if media >= 7:
    print("sua média foi muito boa, parabéns!")
else:
    print(" sua media não foi muito boa, estude mais")
