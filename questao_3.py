# 3- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

F = float(input('Informe a temperatura em Fahrenheit (°F): '))
C = 5 * ((F-32) / 9)

print(f'{F:.1f}°F equivale a {C:.1f}°C')