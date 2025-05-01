# Exercício 1 - Contagem de Notas

quantidade_notas = 0

while True:
    nota = float(input('Digite a nota (ou uma nota negativa para sair)! '))
    if nota < 0:
        break
    if 0 <= nota <= 10:
        quantidade_notas += 1

print(quantidade_notas)

# Exercício 2 - Tabuada de um número

total = 0

while True:
    preco = float(input('Digite o preço do produto (0 para encerrar)! '))
    if preco == 0:
        break
    total += preco

if total > 100:
    total *= 0.9 

print(total)
