conjuntos_usuario = []   # onde todos os conjuntos do usuário serão armazenados.
nome_conjuntos = []      # o índice de cada nome de conjunto corresponde
                         # ao índice de um conjunto da variável anterior.
conjunto_zero = [] # conjunto vazio, serve como padrão na criação de conjuntos.

def menu_principal():

    print("\n" + "~"*71)
    print(f'{'Lista de opções:':^71}')
    print("~"*71)
    print('[0] Finalizar o programa.')
    print('[1] Exibir todos os conjuntos existentes.')
    print('[2] Criar um conjunto.')
    print('[3] Deletar um conjunto.')
    print('[4] Adicionar um elemento a um conjunto existente.')
    print('[5] Remover um elemento de conjunto existente.')
    print('[6] Unir um conjunto existente a outro.')
    print('[7] Exibe os elementos que aparecem em ambos os conjuntos escolhidos.')
    print("~"*71 + "\n")

    selecao = input('Escolha uma opção!')
    return selecao

def mostrar_conjuntos():

    print("-"*24)
    print('|'+' Conjuntos do Usuário '+'|')
    print("-"*24)

    for i in range(len(conjuntos_usuario)):
        print(f'| {nome_conjuntos[i]}: {conjuntos_usuario[i]}')
        print("-"*24)

def cria_conjunto(conjunto : list, nome_do_conjunto : str):

    if nome_do_conjunto not in nome_conjuntos:

        nome_conjuntos.append(nome_do_conjunto)
        conjuntos_usuario.append(conjunto)
        print(f'\nConjunto {nome_do_conjunto} adicionado com sucesso.')

    else:
        print(f'\nErro: Já há um conjunto com o nome {nome_do_conjunto}.')

def deleta_conjunto(nome_do_conjunto : str):

    if nome_do_conjunto in nome_conjuntos:

        index_conjunto = nome_conjuntos.index(nome_do_conjunto)
        conjuntos_usuario.pop(index_conjunto)
        nome_conjuntos.remove(nome_do_conjunto)

        print(f'\nConjunto {nome_do_conjunto} deletado com sucesso.')

    else:
        print(f'\nErro: O conjunto {nome_do_conjunto} não existe.')

def adiciona_elemento(elemento : int, conjunto : str):

    if conjunto in nome_conjuntos:

        index_conjunto = nome_conjuntos.index(conjunto)

        if elemento not in conjuntos_usuario[index_conjunto]:
            conjuntos_usuario[index_conjunto].append(elemento)
            print(f'\nElemento {elemento} adicionado em {conjunto} com sucesso.')
        else:
            print(f'\nErro: Elemento {elemento} já estava em {conjunto}.')
    else:
        print(f'\nErro: O conjunto {conjunto} não existe.')

def remove_elemento(elemento : int, conjunto : str):

    if conjunto in nome_conjuntos:

        index_conjunto = nome_conjuntos.index(conjunto)

        if elemento in conjuntos_usuario[index_conjunto]:

            conjuntos_usuario[index_conjunto].remove(elemento)
            print(f'\nElemento {elemento} removido de {conjunto} com sucesso.')

        else:
            print(f'\nErro: O elemento {elemento} não existe em {conjunto}.')

    else:
        print(f'\nErro: O conjunto {conjunto} não existe.')

def uniao_conjuntos(conjunto1 : str, conjunto2 : str):

    if conjunto1 in nome_conjuntos and conjunto2 in nome_conjuntos:

        index_conjunto = nome_conjuntos.index(conjunto1)
        index_conjunto2 = nome_conjuntos.index(conjunto2)
        copia_conjunto1 = conjuntos_usuario[index_conjunto].copy()
        copia_conjunto2 = conjuntos_usuario[index_conjunto2].copy()

        for elemento in copia_conjunto1:

            if elemento in conjuntos_usuario[index_conjunto2]:

                copia_conjunto2.remove(elemento)

        copia_conjunto1.extend(copia_conjunto2)

        print(f'\nUnião entre os conjuntos {conjunto1} e {conjunto2}!')
        print("-"*20)
        print(f'| {copia_conjunto1}')
        print("-"*20)

    elif conjunto1 not in nome_conjuntos and conjunto2 not in nome_conjuntos:

        print(f'\nErro: O conjunto {conjunto1} e {conjunto2} não existem.')

    elif conjunto1 not in nome_conjuntos:

        print(f'\nErro: O conjunto {conjunto1} não existe.')

    else:

        print(f"\nErro: O conjunto {conjunto2} não existe.")

def intersecao_conjuntos(conjunto1 : str, conjunto2 : str):

    intersecao = []

    if conjunto1 in nome_conjuntos and conjunto2 in nome_conjuntos:

        index_conjunto = nome_conjuntos.index(conjunto1)
        index_conjunto2 = nome_conjuntos.index(conjunto2)

        for elemento in conjuntos_usuario[index_conjunto]:

            if elemento in conjuntos_usuario[index_conjunto2]:

                intersecao.append(elemento)

        if intersecao != []:

            print(f'\nInterseção entre os conjuntos {conjunto1} e {conjunto2}!')
            print("-"*20)
            print(f'| {intersecao}')
            print("-"*20)

        else:

            print(f'\nNenhum elemento intersecta ambos os conjuntos {conjunto1} e {conjunto2}.')

    elif conjunto1 not in nome_conjuntos and conjunto2 not in nome_conjuntos:

        print(f'\nErro: Os conjuntos {conjunto1} e {conjunto2} não existem.')

    elif conjunto1 not in nome_conjuntos:

        print(f'\nErro: O conjunto {conjunto1} não existe.')

    else:

        print(f"\nErro: O conjunto {conjunto2} não existe.")
print('~'*80)
print(f'{'Construtor de Conjuntos Matemáticos':^71}')
print(f'{'Desenvolvido por: Arthur Herbster Fernandes Vogel e Willyam Andrade Medeiros':^71}')
print(f'{'Prof.Dr.Thomaz Maia de Almeida':^71}')
print(f'{'Disciplina: Programação Estruturada':^71}')
print(f'{'Entre: 20/05/2025 - 23/05/2025':^71}')
print('~'*80)


while True:

    selecao = menu_principal()

    if selecao == '0':
        confirmar = input("Digite 'confirmar' para finalizar o programa!")
        if confirmar == "confirmar":
            break
        else:
            print('\nPrograma não finalizado.')

    elif selecao == '1':
        mostrar_conjuntos()

    elif selecao == '2':
        conjunto = input('Digite o nome do conjunto a ser criado!')
        cria_conjunto(conjunto_zero.copy(), conjunto)

    elif selecao == '3':
        conjunto = input('Digite o nome do conjunto a ser deletado!')
        deleta_conjunto(conjunto)

    elif selecao == '4':
        elemento = int(input('Digite o elemento a ser adicionado no conjunto!'))
        conjunto = input('Digite o nome do conjunto!')
        adiciona_elemento(elemento, conjunto)

    elif selecao == '5':
        elemento = int(input('Digite o elemento a ser removido do conjunto!'))
        conjunto = input('Digite o nome do conjunto!')
        remove_elemento(elemento, conjunto)

    elif selecao == '6':
        conjunto = input('Digite o nome do conjunto para unir!')
        conjunto2 = input('Digite o nome do outro conjunto para unir!')
        uniao_conjuntos(conjunto, conjunto2)

    elif selecao == '7':
        conjunto = input('Digite o nome do conjunto para intersectar!')
        conjunto2 = input('Digite o nome do outro conjunto para intersectar!')
        intersecao_conjuntos(conjunto, conjunto2)

    else:
        print("\nErro: Opção inválida.")

print('Programa finalizado com sucesso!')
