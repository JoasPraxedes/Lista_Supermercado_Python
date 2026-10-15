from modulo_variaveis import (
lista_hortifruti_frutas,
lista_hortifruti_legumes,
lista_hortifruti_verduras
)

from modulo_gerenciar_subcategoria import gerenciar_subcategoria

def hortifruti():
    while True:
        print('HORTIFRÚTI\n')

        print('1 - Frutas')
        print('2 - Legumes')
        print('3 - Verduras')
        print('4 - Voltar ao Menu Principal')

        try:
            escolha = int(input('Escolha a opção: '))
        except ValueError as err:
            print('Deve ser uma das opções do HORTIFRÚTI!')
            continue

        if escolha == 1:
            gerenciar_subcategoria('Frutas', lista_hortifruti_frutas)

        elif escolha == 2:
            gerenciar_subcategoria('Legumes', lista_hortifruti_legumes)

        elif escolha == 3:
            gerenciar_subcategoria('Verduras', lista_hortifruti_verduras)

        elif escolha == 4:
            break
