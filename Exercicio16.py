# a=int(input('Digite o primeiro número'))
# b=int(input('Digite o segundo número'))
# c=int(input('Digite o terceiro número'))
# if(a>b):
#     if(a>c):
#         print('O Primero é o maior!')
#     else:
#         print('O terceiro é o maior!')
# elif(b>c):
#     print('O sengundo é o maior!')
# else:
#     print('O terceiro é o maior!')

# a=int(input('Digite o primeiro número'))
# b=int(input('Digite o segundo número'))
# c=int(input('Digite o terceiro número'))
# if(a==b==c):
#     print('Os 3 valores são iguais')
# elif(a>b and a>c):
#     print('O Primero é o maior!')
# elif(b>c):
#     print('O Segundo é o maior!')
# else:
#     print('O Terceiro é o maior!')

a=int(input('Digite o primeiro número'))
b=int(input('Digite o segundo número'))
c=int(input('Digite o terceiro número'))
valores=[a,b,c]
valores.sort()
valores.reverse()
print(valores[0])