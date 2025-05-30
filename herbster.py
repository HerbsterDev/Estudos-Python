def menor_maior(lista):
    if not lista:
        print('A lista está vazia!')
        return
    
    menor = lista[0]
    maior = lista[0]

    for num in lista:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    
    print(f'Menor valor {menor}')
    print(f'Maior valor {maior}')

numeros = [10, 5, 8, 20, 3, 15]
menor_maior(numeros)
