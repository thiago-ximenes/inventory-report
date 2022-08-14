import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    __type_strategy = {
        "simples": SimpleReport,
        "completo": CompleteReport,
    }

    def __get_archive_data(self, file_path):
        with open(file_path, "r") as file:
            if file_path.endswith(".csv"):
                report_data = list(csv.DictReader(file))
            if file_path.endswith(".json"):
                report_data = json.load(file)
            if file_path.endswith(".xml"):
                xml_file = file.read()
                xml_to_json = xmltodict.parse(xml_file)
                report_data = xml_to_json["dataset"]["record"]

        return report_data

    def __generate_report(self, data, strategy):
        return self.__type_strategy[strategy].generate(data)

    @classmethod
    def import_data(cls, file_path, report_type):
        data = cls().__get_archive_data(file_path)
        return cls().__generate_report(data, report_type)
