from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        26736128,
        "Pão Francês",
        "Padaria Renascer",
        "2022-13-08",
        "2023-14-08",
        "padaria-renascer-pao-frances_01",
        "Tempera ambiente",
    )

    assert produto.id == 26736128
    assert produto.nome_do_produto == "Pão Francês"
    assert produto.nome_da_empresa == "Padaria Renascer"
    assert produto.data_de_fabricacao == "2022-13-08"
    assert produto.data_de_validade == "2023-14-08"
    assert produto.numero_de_serie == "padaria-renascer-pao-frances_01"
    assert produto.instrucoes_de_armazenamento == "Tempera ambiente"
