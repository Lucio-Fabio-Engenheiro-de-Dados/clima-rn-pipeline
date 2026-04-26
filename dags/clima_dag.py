from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/project/scripts')

from coleta_clima import coletar_clima
from exporta_csv import exportar_csv
from alerta_telegram import enviar_telegram

default_args = {
    "owner": "airflow",
    "start_date": datetime(2026, 4, 12),
    "retries": 1
}

with DAG(
    dag_id="clima_rn",
    default_args=default_args,
    schedule="0 7 * * *",
    catchup=False,
    tags=["clima", "rn", "telegram", "csv"]
) as dag:

    tarefa_coleta = PythonOperator(
        task_id="coletar_clima",
        python_callable=coletar_clima
    )

    tarefa_exportacao = PythonOperator(
        task_id="exportar_csv",
        python_callable=exportar_csv
    )

    tarefa_alerta = PythonOperator(
        task_id="enviar_alerta_telegram",
        python_callable=enviar_telegram
    )

    tarefa_coleta >> tarefa_exportacao >> tarefa_alerta