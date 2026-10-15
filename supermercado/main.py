# Menu Principal do APP
import modulo_variaveis as vars
from modulo_gerar_pdf import gerar_pdf_compras
from modulo_bebidas import bebidas
from modulo_limpeza_higiene import limpeza_higiene
from modulo_mercearia import mercearia
from modulo_acougue import acougue
from modulo_padaria import padaria
from modulo_peixaria import peixaria
from modulo_hortifruti import hortifruti


while True:
    print('MENU PRINCIPAL\n')

    print('1 - Mercearia')
    print('2 - Açougue')
    print('3 - Peixaria')
    print('4 - Hortifrúti')
    print('5 - Padaria')
    print('6 - Bebidas')
    print('7 - Material de Limpeza e Higiene')
    print('0 - Sair\n')

    try:
        escolha = int(input('Escolha a opção: '))
    except ValueError as err:
        print('Deve ser uma das opções do MENU!')
        continue

    if escolha == 1:
        mercearia()

    elif escolha == 2:
        acougue()

    elif escolha == 3:
        peixaria()

    elif escolha == 4:
        hortifruti()

    elif escolha == 5:
        padaria()

    elif escolha == 6:
        bebidas()

    elif escolha == 7:
        limpeza_higiene()

    # Para encerrar o programa
    elif escolha == 0:
        # Agrupa todas as listas do seu app em um dicionário
        todas_as_listas = {
            "Mercearia (Grãos, Massas e Farinhas)": vars.lista_mercearia_gcl,
            "Mercearia (Temperos, Óleos e Confeitaria)": vars.lista_mercearia_toc,
            "Mercearia (Matinais e Enlatados)": vars.lista_mercearia_me,
            "Mercearia (Doces e Salgados)": vars.lista_mercearia_ds,
            "Açougue (Bovinos)": vars.lista_acougue_bovinos,
            "Açougue (Aves)": vars.lista_acougue_ave,
            "Açougue (Suínos)": vars.lista_acougue_suinos,
            "Açougue (Embutidos)": vars.lista_acougue_embutidos,
            "Peixaria (Peixes Frescos e Resfriados)": vars.lista_peixaria_peixes,
            "Peixaria (Frutos do Mar)": vars.lista_peixaria_frutos_mar,
            "Peixaria (Congelados)": vars.lista_peixaria_congelados,
            "Hortifrúti (Frutas)": vars.lista_hortifruti_frutas,
            "Hortifrúti (Legumes)": vars.lista_hortifruti_legumes,
            "Hortifrúti (Verduras)": vars.lista_hortifruti_verduras,
            "Padaria (Pães)": vars.lista_padaria_paes,
            "Padaria (Salgados)": vars.lista_padaria_salgados,
            "Padaria (Doces)": vars.lista_padaria_doces,
            "Bebidas (Bebidas não alcoólica)": vars.lista_bebidas_nao_alcoolicas,
            "Bebidas (Bebidas alcoólica)": vars.lista_bebidas_alcoolicas,
            "Produtos (Limpeza)": vars.lista_produto_limpeza,
            "Produtos (Higiene)": vars.lista_produto_higiene
        }

        # Gera o PDF formatado
        gerar_pdf_compras(todas_as_listas)
        break
