from modulo_variaveis import (
    lista_acougue_bovinos,
    lista_acougue_ave,
    lista_acougue_suinos,
    lista_acougue_embutidos
)
from modulo_gerenciar_subcategoria import gerenciar_subcategoria


def acougue():
    while True:
        print('AÇOUGUE')
        print('1 - Bovinos')
        print('2 - Aves')
        print('3 - Suínos')
        print('4 - Embutidos')
        print('5 - Voltar ao Menu Principal')

        try:
            escolha = int(input('Escolha a opção: '))
        except ValueError as err:
            print('Deve ser uma das opções do AÇOUGUE!')
            continue

        if escolha == 1:
            gerenciar_subcategoria('Bovinos',lista_acougue_bovinos)

        elif escolha == 2:
            gerenciar_subcategoria('Aves',lista_acougue_ave)

        elif escolha == 3:
            gerenciar_subcategoria('Suínos',lista_acougue_suinos)

        elif escolha == 4:
            gerenciar_subcategoria('Embutidos',lista_acougue_embutidos)

        elif escolha == 5:
            break
