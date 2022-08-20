# Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

# a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;

# b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;

# c) A mensagem "Aprovado com "Distinção", se a média for igual a 10.

n1 = float(input("Informe a nota 1: "))
n2 = float(input("Informe a nota 2: "))
n3 = float(input("Informe a nota 3: "))

media = (n1 + n2 + n3) / 3

print('Média: {:.1f}'.format(media))

if media > 7 and media < 10:
    print('Aprovado!')
if media < 7:
    print('Reprovado!')
elif media == 10:
    print('Aprovado com Distinção!')