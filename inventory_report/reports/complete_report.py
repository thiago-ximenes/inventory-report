from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __get_stock_by_company(stock):
        return {
            company["nome_da_empresa"]: [
                product
                for product in stock
                if product["nome_da_empresa"] == company["nome_da_empresa"]
            ]
            for company in stock
        }

    def __create_report_by_company(stock):
        report = "Produtos estocados por empresa:\n"
        for company, products in stock.items():
            report += f"- {company}: {len(products)}\n"
        return report

    @classmethod
    def generate(self, list):
        stock_by_company = self.__get_stock_by_company(list)
        stock_by_company_report = self.__create_report_by_company(
            stock_by_company
        )
        simple_report = super().generate(list)
        complete_report = simple_report + "\n" + stock_by_company_report

        return complete_report
