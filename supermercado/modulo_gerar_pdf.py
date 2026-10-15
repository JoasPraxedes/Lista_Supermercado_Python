from fpdf import FPDF


def gerar_pdf_compras(dicionario_setores):
    pdf = FPDF()
    pdf.add_page()

    # Cabeçalho / Título do PDF
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Lista de Compras do Supermercado", ln=True, align="C")
    pdf.ln(10)

    # Percorre cada setor e seus respectivos produtos
    for setor, itens in dicionario_setores.items():
        # Só imprime o setor se houver itens adicionados nele
        if itens:
            # Nome da categoria/setor em negrito
            pdf.set_font("Arial", "B", 14)
            pdf.set_text_color(33, 37, 41)  # Tom escuro profissional
            pdf.cell(0, 8, f"--- {setor.upper()} ---", ln=True)

            # Itens do setor
            pdf.set_font("Arial", "", 12)
            for item in itens:
                pdf.cell(0, 6, f"  [  ] {item}", ln=True)  # Adiciona um checkbox [ ] legal para riscar no mercado!

            pdf.ln(5)  # Espaço entre os setores

    # Salva o arquivo final
    pdf.output("ListaSupermercado.pdf")
    print("\nPDF gerado com sucesso como 'ListaSupermercado.pdf'! Boas compras!")