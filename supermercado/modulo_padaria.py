from modulo_variaveis import (
    lista_padaria_paes,
    lista_padaria_salgados,
    lista_padaria_doces
)

from modulo_gerenciar_subcategoria import gerenciar_subcategoria

def padaria():
    while True:
        print('PADARIA\n')

        print('1 - Pães')
        print('2 - Salgados')
        print('3 - Doces')
        print('4 - Voltar ao Menu Principal')

        try:
            escolha = int(input('Escolha a opção: '))
        except ValueError as err:
            print('Deve ser uma das opções do PADARIA!')
            continue

        if escolha == 1:
            gerenciar_subcategoria('Pães', lista_padaria_paes)

        elif escolha == 2:
            gerenciar_subcategoria('Salgados', lista_padaria_salgados)

        elif escolha == 3:
            gerenciar_subcategoria('Doces', lista_padaria_doces)

        elif escolha == 4:
            break