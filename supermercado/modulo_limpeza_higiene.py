from modulo_variaveis import (
    lista_produto_limpeza,
    lista_produto_higiene
)

from modulo_gerenciar_subcategoria import gerenciar_subcategoria

def limpeza_higiene():
    while True:
        print('LIMPEZA E HIGIENE')

        print('1 - Produtos de Limpeza')
        print('2 - Produtos de Higiene')
        print('3 - Voltar ao Menu Principal')

        try:
            escolha = int(input('Escolha a opção: '))
        except ValueError as err:
            print('Deve ser uma das opções do LIMPEZA E HIGIENE!')
            continue

        if escolha == 1:
            gerenciar_subcategoria('Produtos de Limpeza', lista_produto_limpeza)

        elif escolha == 2:
            gerenciar_subcategoria('Produtos de Higiene', lista_produto_higiene)

        elif escolha == 3:
            break