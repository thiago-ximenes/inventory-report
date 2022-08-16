from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        else:
            with open(file_path, "r") as file:
                xml_file = file.read()
                xml_to_json = xmltodict.parse(xml_file)
                report_data = xml_to_json["dataset"]["record"]
                return report_data
