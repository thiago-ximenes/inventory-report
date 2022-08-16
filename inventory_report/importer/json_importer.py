import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        else:
            with open(file_path, "r") as file:
                json_file = file.read()
                report_data = json.loads(json_file)
                return report_data
