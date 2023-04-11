from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def readCsv(cls, path, type):
        with open(path) as file:
            if type == "simples":
                return SimpleReport.generate(list(csv.DictReader(file)))
            if type == "completo":
                return CompleteReport.generate(list(csv.DictReader(file)))

    @classmethod
    def readJson(cls, path, type):
        with open(path) as fileJson:
            if type == "simples":
                return SimpleReport.generate(json.load(fileJson))
            if type == "completo":
                return CompleteReport.generate(json.load(fileJson))

    @classmethod
    def import_data(cls, path, type):
        if ".csv" in path:
            return Inventory.readCsv(path, type)

        if ".json" in path:
            return Inventory.readJson(path, type)
