# 6- Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

recebe_idade = []
recebe_altura = []

for pessoa in range (1, 6):
    print(f'Cadastro {pessoa}ª pessoa'.format())
    idade = int(input('Informe a idade: '))
    altura = float(input('Informe a altura: '))
    recebe_idade.append(idade)
    recebe_altura.append(altura)

print('--' * 25)
print('Ordem inversa:')
print(f'Alturas: {recebe_altura[::-1]}')
print(f'Idades: {recebe_idade[::-1]}')    