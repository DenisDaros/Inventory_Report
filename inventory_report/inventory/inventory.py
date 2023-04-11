from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path) as file:
            if type == "simples":
                return SimpleReport.generate(list(csv.DictReader(file)))

            if type == "completo":
                return CompleteReport.generate(list(csv.DictReader(file)))
