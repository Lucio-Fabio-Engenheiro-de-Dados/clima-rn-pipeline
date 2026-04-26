import os
from datetime import datetime
import mysql.connector
import pandas as pd

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="admin",
        password="admin",
        database="clima"
    )

def exportar_csv():
    conexao = conectar_banco()

    query = """
        SELECT
            id,
            cidade,
            latitude,
            longitude,
            temperatura,
            descricao,
            chuva,
            data_coleta
        FROM clima_dados
        WHERE DATE(data_coleta) = CURDATE()
        ORDER BY cidade, data_coleta
    """

    df = pd.read_sql(query, conexao)
    conexao.close()

    os.makedirs("data", exist_ok=True)

    data_arquivo = datetime.now().strftime("%Y-%m-%d")
    caminho = f"data/clima_{data_arquivo}.csv"

    df.to_csv(caminho, index=False, encoding="utf-8-sig")

    print(f"CSV gerado com sucesso: {caminho}")

if __name__ == "__main__":
    exportar_csv()