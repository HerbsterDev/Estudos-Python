# Exercício 1 - Calculadora de Fatorial

numero = int(input('Digite um número inteiro positivo! '))

if numero < 0:
    print('Número inválido! Insira um número positivo.')
else:
    fatorial = 1
    contador = 1
    
    while contador <= numero:
        fatorial *= contador
        contador += 1

    print(f'O fatorial de {numero} é {fatorial}')

# Exercício 2 - Gera um número aleatório entre 1 e 100

import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input('Digite seu palpite (entre 1 e 100)! '))
    
    if palpite < numero_secreto:
        print('Maior')
    elif palpite > numero_secreto:
        print('Menor')
    else:
        print('Parabéns! Você acertou o número!')
        break
