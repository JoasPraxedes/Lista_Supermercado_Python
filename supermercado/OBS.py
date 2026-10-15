"""
OBS: quando tiver -> lógica antiga, é para indicar como funciona o programa antes das modificações.
Desse primeiro modo, era necessário criar variáveis  no modulo_variaveis para manipular o programa,
no momento está da seguinte forma:

        if opcao == 1:
            try:
                #while modulo_variaveis.produto_mercearia != 'sair':  -> lógica antiga

            #for modulo_variaveis.produto_mercearia in lista_mercearia:-> lógica antiga
                #print(modulo_variaveis.produto_mercearia)-> lógica antiga

            #for produto_mercearia in lista_mercearia:
                #print(produto_mercearia)



        elif opcao == 2:

            try:
                #while modulo_variaveis.produto_para_remover != 'sair':-> lógica antiga

            #for modulo_variaveis.produto_mercearia in lista_mercearia:-> lógica antiga
                #print(modulo_variaveis.produto_mercearia)-> lógica antiga

        elif opcao == 3:
            break


2 - OBS: O código abaixo virar uma função genéria que irá ser utilizado em todo o sistema
def mostrar_lista():
    print('\nLista de Mercearia: \n')
    for produto_mercearia in lista_mercearia:
        print(produto_mercearia)

def mercearia():
    while True:
        print('MERCEARIA')

        print(' 1 - Adicionar Produto')
        print(' 2 - Remover Produto')
        print(' 3 - Voltar ao Menu Principal')

        try:
            opcao = int(input('Escolha a sua opção: '))
        except ValueError:
            print('Deve ser uma das opções do MENU!')
            continue

        if opcao == 1:
            try:
                while True:
                    print("Escreva o produto para adicionar a lista de Mercearia ou digite 'sair': ")
                    produto_mercearia = input()
                    if produto_mercearia != 'sair':
                        lista_mercearia.append(produto_mercearia)
                    else:
                        break
            except ValueError as err:
                print(f'Ocorreu um problema {err}')

            mostrar_lista()

        elif opcao == 2:
            mostrar_lista()

            try:
                while True:
                    print("Digite o produto para remover da Lista de Mercearia ou 'sair': ")
                    produto_para_remover = input()
                    if produto_para_remover != 'sair':
                        lista_mercearia.remove(produto_para_remover)
                    else:
                        break
            except ValueError:
                print('Não está na lista de Mercearia!')
                continue

            mostrar_lista()

        elif opcao == 3:
            break
"""