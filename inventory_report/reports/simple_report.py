from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def data_antiga(cls, lista):
        lista_datas = [i["data_de_fabricacao"] for i in lista]
        data_antiga = min(lista_datas)
        return data_antiga

    @classmethod
    def data_validade(cls, lista):
        today_data = datetime.today().strftime("%Y-%m-%d")
        lista_datas = [
            i["data_de_validade"]
            for i in lista
            if i["data_de_validade"] >= today_data
        ]
        data_validade = min(lista_datas)
        return data_validade

    @classmethod
    def empresa_mais_produtos(cls, lista):
        lista_empresas = [i["nome_da_empresa"] for i in lista]
        empresas = Counter(lista_empresas)
        return empresas.most_common(1)[0][0]

    @classmethod
    def generate(cls, lista):
        old_data = cls.data_antiga(lista)
        data_valid = cls.data_validade(lista)
        company = cls.empresa_mais_produtos(lista)
        return (
            f"Data de fabricação mais antiga: {old_data}\n"
            f"Data de validade mais próxima: {data_valid}\n"
            f"Empresa com mais produtos: {company}"
        )
