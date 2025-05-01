# Exercício 1 - Desconto no supermercado

valor_compra = float(input('Digite o valor total da compra: R$ '))

if valor_compra > 200:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f'Você recebeu 10% de desconto. Valor a pagar: R$: {valor_final}')
else:
    print('Sem desconto. Valor a pagar: R$', valor_compra)

# Exercício 2 - Verificador de hora extra

horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas hoje: "))

if horas_trabalhadas > 8:
    horas_extras = horas_trabalhadas - 8
    print(f'Houve hora extra. Total de horas extras:{horas_extras}')
else:
    print('Não houve hora extra.')
