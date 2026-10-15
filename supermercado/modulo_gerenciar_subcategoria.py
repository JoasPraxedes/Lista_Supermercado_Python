def mostrar_lista(nome_categoria,lista_alvo):
    print(f"\nLista de {nome_categoria}:\n")
    for produto in lista_alvo:
        print(produto)


def gerenciar_subcategoria(nome_categoria, lista_alvo):
    while True:
        print(f'\n--- {nome_categoria.upper()} ---')
        print(' 1 - Adicionar Produto')
        print(' 2 - Remover Produto')
        print(' 3 - Voltar')

        try:
            opcao = int(input('Escolha a sua opção: '))
        except ValueError:
            print('Deve ser uma das opções do MENU!')
            continue

        if opcao == 1:
            while True:
                produto = input(f"Escreva o produto para adicionar em {nome_categoria} ou 'sair': ")
                if produto.lower() != 'sair':
                    lista_alvo.append(produto)
                else:
                    break

            # Mostra a lista atualizada dinamicamente
            mostrar_lista(nome_categoria, lista_alvo)

        elif opcao == 2:
            mostrar_lista(nome_categoria, lista_alvo)

            while True:
                produto = input(f"Digite o produto para remover de {nome_categoria} ou 'sair': ")
                if produto.lower() == 'sair':
                    break
                if produto in lista_alvo:
                    lista_alvo.remove(produto)
                    print(f"'{produto}' removido com sucesso!")
                else:
                    print(f"'{produto}' não está na lista de {nome_categoria}!")

            mostrar_lista(nome_categoria, lista_alvo)

        elif opcao == 3:
            break