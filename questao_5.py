# 5- Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input('Digite um número: ')
lista = []

for i in range (numero + 1):
    if i % 2 == 1 and i != 2:
         lista.append(i)
    if i == 2:
         lista.append(i)
print('Número: {lista}')
