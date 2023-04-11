from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
from xml.etree import ElementTree as ET


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
    def readXml(cls, path, type):
        tree = ET.parse(path)
        root = tree.getroot()

        fileXlm = root.findall("record")
        list_file_xml = []

        for list in fileXlm:
            list_file_xml.append({i.tag: i.text for i in list})

        if type == "simples":
            return SimpleReport.generate(list_file_xml)
        if type == "completo":
            return CompleteReport.generate(list_file_xml)

    @classmethod
    def import_data(cls, path, type):
        if ".csv" in path:
            return Inventory.readCsv(path, type)

        if ".json" in path:
            return Inventory.readJson(path, type)

        if ".xml" in path:
            return Inventory.readXml(path, type)
        # https://www.youtube.com/watch?v=YV_emEzpPyM
