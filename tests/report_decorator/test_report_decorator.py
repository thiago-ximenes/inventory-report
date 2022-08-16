from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.colored_report import ColoredReport


BLUE = "\033[36m"
RED = "\033[31m"
GREEN = "\033[32m"
END = "\033[0m"


def test_decorar_relatorio():
    csv_path = "inventory_report/data/inventory.csv"

    colored_csv_report = ColoredReport(SimpleReport).generate(
        CsvImporter.import_data(csv_path)
    )
    assert colored_csv_report == (
        f"{GREEN}Data de fabricação mais antiga:{END} "
        f"{BLUE}2020-09-06{END}\n"
        f"{GREEN}Data de validade mais próxima:{END} "
        f"{BLUE}2023-09-17{END}\n"
        f"{GREEN}Empresa com mais produtos:{END} "
        f"{RED}Target Corporation{END}"
    )
