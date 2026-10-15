from modulo_variaveis import (
    lista_mercearia_gcl,
    lista_mercearia_toc,
    lista_mercearia_me,
    lista_mercearia_ds,
)
from modulo_gerenciar_subcategoria import gerenciar_subcategoria

def mercearia():
    while True:
        print('Mercearia')

        print('1 - Grãos, Massas e Farinhas')
        print('2 - Temperos, Óleos e Confeitaria')
        print('3 - Matinais e Enlatados')
        print('4 - Doces e Salgados')
        print('5 - Voltar ao Menu Principal')

        try:
            escolha = int(input('Escolha a opção: '))
        except ValueError as err:
            print('Deve ser uma das opções do AÇOUGUE!')
            continue

        if escolha == 1:
            gerenciar_subcategoria('Grãos, Cereais e Leguminosas', lista_mercearia_gcl)

        elif escolha == 2:
            gerenciar_subcategoria('Temperos, Óleos e Confeitaria', lista_mercearia_toc)

        elif escolha == 3:
            gerenciar_subcategoria('Matinais e Enlatados', lista_mercearia_me)

        elif escolha == 4:
            gerenciar_subcategoria('Doces e Salgados', lista_mercearia_ds)

        elif escolha == 5:
            break
