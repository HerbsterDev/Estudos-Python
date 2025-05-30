# Exercício 1 - Tamanho de String.

str = input('Digite alguma coisa! ')
tamanho = len(str)
print(f'{tamanho} caracteres')

# Exercício 2 - Maior String
str1 = input('Digite algo!')
str2 = input('Digite algo! ')
tamanho1 = len(str1)
tamanho2 = len(str2)
if tamanho1 > tamanho2:
    print(f'{str1} é maior')
elif tamanho1 < tamanho2:
    print(f'{str2} é maior')
