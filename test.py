
'''
 Programa que soma dois numeros
 E exibi o resultado da soma
'''
# value1 = int(input("Entre com o primeiro valor: "))
# value2 = int(input("Entre com o segundo valor: "))

# soma =  value1 + value2

# print(f"A soma de {value1} e {value2} é igual a {soma} ")


import sys

try:
    value1 = int(input("Entre com o primeiro valor: "))
    value2 = int(input("Entre com o segundo valor: "))
except ValueError:
    print(f"Coloque um Número !")
    sys.exit(1)
soma =  value1 + value2

print(f"A soma de {value1} e {value2} é igual a {soma} ")