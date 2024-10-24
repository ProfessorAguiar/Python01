frutas = ["maça", "banana", "cereja"]
frutas.append('melão')
frutas.append('abacaxi')
frutas.sort()
frutas.reverse()
print(len(frutas))
for i in range(len(frutas)):
    if(frutas[i]=="banana"):
        frutas.pop(i)
        # break
print(frutas)
# frutas.append(input('Digite uma fruta: '))
# print(len(frutas))