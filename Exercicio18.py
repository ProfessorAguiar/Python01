nota1=float(input('Digite a Primeira nota: '))
nota2=float(input('Digite a Segunda nota: '))
media=(nota1+nota2)/2
print(f'A média do aluno é: {media}')
if(media<4):
    print('Reprovado direto')
elif(media>7):
    print('Aprovado direto')
else:
    print('Aluno em Recuperação')
    rec=float(input('Digite a nota de recuperação: '))
    if(rec<5):
        print('Reprovado na Recuperação')
    else:
        print('Aprovado na Recuperação')