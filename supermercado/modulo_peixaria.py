from modulo_variaveis import (
    lista_peixaria_peixes,
    lista_peixaria_frutos_mar,
    lista_peixaria_congelados
)
from modulo_gerenciar_subcategoria import gerenciar_subcategoria

def peixaria():
    while True:
        print('PEIXARIA\n')

        print('1 - Peixes Frescos e Resfriados')
        print('2 - Frutos do Mar')
        print('3 - Congelados')
        print('4 - Voltar ao Menu Principal')

        try:
            escolha = int(input('Escolha a opção: '))
        except ValueError as err:
            print('Deve ser uma das opções do PEIXARIA!')
            continue

        if escolha == 1:
            gerenciar_subcategoria('Peixes Frescos e Resfriados',lista_peixaria_peixes)

        elif escolha == 2:
            gerenciar_subcategoria('Frutos do Mar', lista_peixaria_frutos_mar)

        elif escolha == 3:
            gerenciar_subcategoria('Congelados', lista_peixaria_congelados)

        elif escolha == 4:
            break