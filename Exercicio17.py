peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
IMC=peso/(altura*altura)
print(f'Seu IMC é: {IMC}')
if(IMC>25):
    print('Acima do peso ideal.')
else:
    print('Peso ok.')