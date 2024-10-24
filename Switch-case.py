# value=3
# match value:
#     case 1:
#         result='one'
#     case 2:
#         result='two'
#     case 3:
#         result='three'
#     case _:
#         result='default'
# print(result)
total=0
escolha=0
pizzas=[]
valores=[]
while(escolha!=5):
    print('Cardápio: ')
    print('1- calabresa com cebola - R$59,90\n2- camarão com catupiry - R$87,80\n3- frango com requeijão - R$65,50\n4- banana com chocolate - R$59,90')
    print('5- Resumo do pedido')
    escolha=int(input('Digite a opção escolhida (apenas números):'))
    match escolha:
        case 1:
            print('Pizza adicionada')
            pizzas.append('calabresa com cebola')
            valores.append(59.9)
        case 2:
            print('Pizza adicionada')
            pizzas.append('camarão com catupiry')
            valores.append(87.8)
        case 3:
            print('Pizza adicionada')
            pizzas.append('frango com requeijão')
            valores.append(65.5)
        case 4:
            print('Pizza adicionada')
            pizzas.append('banana com chocolate')
            valores.append(59.9)
        case 5:
            for x in range(len(valores)):
                print(f'{x+1}- {pizzas[x]} - R${valores[x]}')
                total+=valores[x]
            print(f'Total: R${round(total,2)}')
        case _:
            print('Escolha uma opção válida!')