# 5- Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input('Digite um número: '))

lista_primos = []
primos = ''

for i in range(1, numero + 1):
        cont = 0
        for x in range (1, i + 1):
             if i % x == 0:
                 cont += 1
        if cont == 2:
            lista_primos.append(i)
            primos = str(lista_primos)[1:-1]
print(f'Números primos entre 1 e {numero}: {primos}')

