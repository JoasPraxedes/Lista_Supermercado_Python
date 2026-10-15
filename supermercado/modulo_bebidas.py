from modulo_variaveis import (
    lista_bebidas_nao_alcoolicas,
    lista_bebidas_alcoolicas
)

from modulo_gerenciar_subcategoria import gerenciar_subcategoria

def bebidas():
    while True:
        print('BEBIDAS')

        print('1 - Bebidas não alcoólica')
        print('2 - Bebidas alcoólica')
        print('3 - Voltar ao Menu Principal')

        try:
            escolha = int(input('Escolha a opção: '))
        except ValueError as err:
            print('Deve ser uma das opções do BEBIDAS!')
            continue

        if escolha == 1:
            gerenciar_subcategoria('Bebidas não alcoólica', lista_bebidas_nao_alcoolicas)

        elif escolha == 2:
            gerenciar_subcategoria('Bebidas alcoólica', lista_bebidas_alcoolicas)

        elif escolha == 3:
            break
