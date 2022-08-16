import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        else:
            with open(file_path, "r") as file:
                report_data = list(csv.DictReader(file))
                return report_data
