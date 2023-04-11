from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        first_report = SimpleReport.generate(lista)
        lista_empresas = dict(Counter([i["nome_da_empresa"] for i in lista]))
        second_report = ""
        for i in lista_empresas:
            second_report += f"- {i}: {lista_empresas[i]}\n"

        return (
            f"{first_report}\n"
            "Produtos estocados por empresa:\n"
            f"{second_report}"
        )
