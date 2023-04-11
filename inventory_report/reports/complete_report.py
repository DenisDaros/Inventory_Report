from inventory_report.reports.simple_report import SimpleReport
# from simple_report import SimpleReport
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


lista_teste = [
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-05-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 2,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-10",
        "data_de_validade": "2023-06-10",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 3,
        "nome_do_produto": "sofá",
        "nome_da_empresa": "denis daros",
        "data_de_fabricacao": "2022-05-10",
        "data_de_validade": "2023-07-10",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
]
teste = CompleteReport.generate(lista_teste)
print(teste)
