from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "chocolate",
        "Willie Wonka",
        "01/01/2022",
        "01/01/2023",
        "1234",
        "estocado",
    )
    assert produto.id == 1
    assert produto.nome_da_empresa == "Willie Wonka"
    assert produto.nome_do_produto == "chocolate"
    assert produto.data_de_fabricacao == "01/01/2022"
    assert produto.data_de_validade == "01/01/2023"
    assert produto.numero_de_serie == "1234"
    assert produto.instrucoes_de_armazenamento == "estocado"
