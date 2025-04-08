# Questão 1
n1=int(input('Digite um número!'))
for i in range(n1 + 1):
    fatorial=1
    for n in range(1, i + 1):
        fatorial=fatorial*n
    print(f'{i}= {fatorial}')


# Questão 2
inicio=int(input('Digite o número inicial!'))
final=int(input('Digite o número final!'))

for num in range(inicio, final+1):
    quant_digito=len(str(num))
    soma_potencia=0
    for digito in str(num):
        soma_potencia=soma_potencia+int(digito)**quant_digito
    if num==soma_potencia:
        print(f'Esses são os números de Armstrong {num}')



