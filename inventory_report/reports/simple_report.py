from datetime import date
from statistics import mode


class SimpleReport:
    def generate(list):
        fabrication_date = min(list, key=lambda x: x["data_de_fabricacao"])[
            "data_de_fabricacao"
        ]
        expiration_date = min(
            list,
            key=lambda x: x["data_de_validade"]
            if x["data_de_validade"] > date.today().strftime("%Y-%m-%d")
            else None,
        )["data_de_validade"]
        company_with_more_products = mode(
            company["nome_da_empresa"] for company in list
        )
        return (
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
