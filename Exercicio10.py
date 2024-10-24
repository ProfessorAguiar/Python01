salario=float(input("digite o seu salário: "))
valorVT=salario*0.06
valorPS=salario*0.03
print(f"O valor do desconto do VT é: R${valorVT}")
print(f"O valor do desconto do PS é: R${valorPS}")
print(f"Seu novo salário com desconto de 6% para vale-transporte e 3% de plano de saúde será: R${salario-valorVT-valorPS} .")