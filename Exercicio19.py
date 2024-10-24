player1=input('Escolha sua opção entre pedra, papel e tesoura: ')
player2=input('Escolha sua opção entre pedra, papel e tesoura: ')
if(player1==player2):
    print('Empate')
elif((player1=='pedra' and player2=='tesoura') or (player1=='papel' and player2=='pedra') or (player1=='tesoura' and player2=='papel')):
    print(f'Player1 venceu!!! ({player1} vence de {player2})')
else:
    print(f'Player2 venceu!!! ({player2} vence de {player1})')