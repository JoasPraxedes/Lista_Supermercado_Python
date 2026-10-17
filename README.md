# 🛒 Lista de Supermercado em Python

Projeto desenvolvido em Python para gerenciamento de listas de compras por setores e subcategorias via terminal, com exportação final em arquivo PDF.

---

## 🎯 Objetivo
Aplicar conceitos fundamentais e intermediários de Python, como:
- Tratamento de exceções (`try-except`)
- Loops de repetição e estruturas condicionais
- Modularização e funções reutilizáveis
- Manipulação de arquivos e geração de relatórios em PDF (`fpdf2`)

---

## 🛠️ Ferramentas Utilizadas
- **Python**: Linguagem principal.
- **PyCharm**: IDE utilizada para desenvolvimento e depuração.
- **FPDF2**: Biblioteca utilizada para formatação do checklist em PDF.

---

## 🏗️ Arquitetura do Projeto
O sistema foi estruturado em módulos independentes:
- `main.py`: Ponto de entrada do programa e fluxo do menu principal.
- **Módulos de Setores**: Mercearia, Açougue, Peixaria, Hortifrúti, Padaria, Bebidas, Limpeza/Higiene.
- **Módulo de Subcategorias**: Função genérica responsável pela adição e remoção de produtos reutilizada por todos os setores.
- **Módulo de PDF**: Responsável pela formatação e exportação dos itens cadastrados para o arquivo `ListaSupermercado.pdf`.

---

## 🚀 Melhorias Futuras
- Implementação de Interface Gráfica (GUI) com `Tkinter` ou `PyQt`.
- Inclusão de estimativa de preços e quantidades.
