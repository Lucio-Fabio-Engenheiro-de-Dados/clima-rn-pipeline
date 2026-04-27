# 🚀 Guia para Iniciantes: Como Fazer o Projeto Clima RN Rodar

Este guia ensina, passo a passo, como executar o projeto **Clima RN** no computador, utilizando as principais tecnologias do projeto:

* Python
* OpenWeather API
* MySQL
* Docker
* Apache Airflow
* GitHub Desktop

---

# 1. Objetivo do Projeto

O **Clima RN** é um projeto de Engenharia de Dados que coleta dados climáticos de cidades do Rio Grande do Norte usando a API OpenWeather, processa essas informações com Python e salva os dados em um banco MySQL.

O projeto também pode ser orquestrado pelo Apache Airflow, permitindo execução automática da coleta.

---

# 2. Estrutura Esperada do Projeto

A pasta do projeto deve estar organizada assim:

```bash
clima_rn/
│
├── dags/
│   └── clima_dag.py
│
├── scripts/
│   ├── coleta_clima.py
│   └── teste_mysql.py
│
├── docs/
│   └── GUIA_SUBIR_PROJETO.md
│
├── arquitetura_clima_rn.png
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# 3. Tecnologias Utilizadas

| Tecnologia     | Função no Projeto                         |
| -------------- | ----------------------------------------- |
| Python         | Executa o script de coleta climática      |
| Requests       | Faz requisições para a API OpenWeather    |
| Python-dotenv  | Lê variáveis do arquivo `.env`            |
| MySQL          | Armazena os dados coletados               |
| Docker         | Sobe os containers do MySQL e Airflow     |
| Apache Airflow | Orquestra e agenda a execução do pipeline |
| GitHub         | Armazena o projeto online                 |

---

# 4. Pré-requisitos

Antes de começar, instale:

1. Python
2. Docker Desktop
3. Git
4. GitHub Desktop
5. VS Code

Depois, teste no terminal:

```bash
python --version
```

```bash
docker --version
```

```bash
git --version
```

Se algum comando não funcionar, a ferramenta ainda não está instalada ou não está configurada no PATH.

---

# 5. Criar o Arquivo `.env`

Na raiz do projeto, crie um arquivo chamado:

```bash
.env
```

Dentro dele, coloque:

```env
API_KEY=sua_chave_da_openweather
DB_HOST=localhost
DB_PORT=3307
DB_USER=admin
DB_PASSWORD=admin
DB_NAME=clima
```

Atenção: substitua `sua_chave_da_openweather` pela sua chave real da API OpenWeather.

---

# 6. Criar o Arquivo `.gitignore`

Na raiz do projeto, crie ou confira o arquivo:

```bash
.gitignore
```

Conteúdo recomendado:

```gitignore
# Variáveis sensíveis
.env

# Python
__pycache__/
*.pyc
.venv/
venv/

# Airflow
logs/
airflow.db
standalone_admin_password.txt

# Docker
*.log

# VS Code
.vscode/

# Dados gerados
*.csv
*.xlsx
*.json
```

O `.gitignore` deve ir para o GitHub, mas o `.env` não deve ir.

---

# 7. Criar o `requirements.txt`

Na raiz do projeto, crie ou edite o arquivo:

```bash
requirements.txt
```

Conteúdo básico:

```txt
requests
mysql-connector-python
python-dotenv
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# 8. Código do Script `coleta_clima.py`

O arquivo deve estar em:

```bash
scripts/coleta_clima.py
```

Código base:

```python
import os
import requests
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY não encontrada. Verifique o arquivo .env na raiz do projeto.")

locais = [
    {"nome": "Natal", "lat": -5.79, "lon": -35.21},
    {"nome": "Parnamirim", "lat": -5.91, "lon": -35.26},
    {"nome": "Macaiba", "lat": -5.86, "lon": -35.35},
    {"nome": "Ceara Mirim", "lat": -5.64, "lon": -35.43},
    {"nome": "Sao Goncalo do Amarante", "lat": -5.79, "lon": -35.32},
    {"nome": "Mossoro", "lat": -5.19, "lon": -37.34},
    {"nome": "Caico", "lat": -6.46, "lon": -37.10},
    {"nome": "Pau dos Ferros", "lat": -6.11, "lon": -38.21}
]


def conectar_banco():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


def coletar_clima():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    for local in locais:
        try:
            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?lat={local['lat']}&lon={local['lon']}"
                f"&appid={API_KEY}&units=metric&lang=pt_br"
            )

            resposta = requests.get(url, timeout=30)

            if resposta.status_code != 200:
                print(f"Erro ao buscar dados de {local['nome']}: {resposta.text}")
                continue

            dados = resposta.json()

            cidade = local["nome"]
            latitude = local["lat"]
            longitude = local["lon"]
            temperatura = dados["main"]["temp"]
            umidade = dados["main"]["humidity"]
            descricao = dados["weather"][0]["description"]
            nuvens = dados["clouds"]["all"]

            chuva = 0.0
            if "rain" in dados and "1h" in dados["rain"]:
                chuva = float(dados["rain"]["1h"])

            data_coleta = datetime.now()

            sql = """
                INSERT INTO clima_dados
                (cidade, latitude, longitude, temperatura, descricao, chuva, data_coleta, umidade, nuvens)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            valores = (
                cidade,
                latitude,
                longitude,
                temperatura,
                descricao,
                chuva,
                data_coleta,
                umidade,
                nuvens
            )

            cursor.execute(sql, valores)
            conexao.commit()

            print(
                f"Salvo com sucesso: {cidade} | "
                f"Temp: {temperatura}°C | "
                f"Umidade: {umidade}% | "
                f"Nuvens: {nuvens}% | "
                f"Chuva: {chuva} mm"
            )

        except Exception as e:
            print(f"Erro geral em {local['nome']}: {e}")

    cursor.close()
    conexao.close()
    print("Coleta finalizada.")


if __name__ == "__main__":
    coletar_clima()
```

---

# 9. Criar o `docker-compose.yml`

Na raiz do projeto, crie o arquivo:

```bash
docker-compose.yml
```

Conteúdo recomendado para iniciante:

```yaml
services:
  mysql:
    image: mysql:8
    container_name: clima_mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: clima
      MYSQL_USER: admin
      MYSQL_PASSWORD: admin
    ports:
      - "3307:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  airflow:
    image: apache/airflow:2.8.1
    container_name: airflow_clima
    restart: always
    depends_on:
      - mysql
    environment:
      AIRFLOW__CORE__EXECUTOR: SequentialExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: sqlite:////opt/airflow/airflow.db
      AIRFLOW__CORE__LOAD_EXAMPLES: "false"
    ports:
      - "8080:8080"
    volumes:
      - ./dags:/opt/airflow/dags
      - ./scripts:/opt/airflow/scripts
      - ./requirements.txt:/requirements.txt
    command: >
      bash -c "pip install -r /requirements.txt &&
      airflow db migrate &&
      airflow users create --username admin --firstname Lucio --lastname Lima --role Admin --email admin@email.com --password admin || true &&
      airflow webserver & airflow scheduler"

volumes:
  mysql_data:
```

---

# 10. Subir os Containers

Abra o terminal na pasta do projeto:

```bash
cd Desktop\clima_rn
```

Suba os containers:

```bash
docker compose up -d
```

Verifique se estão rodando:

```bash
docker ps
```

Você deve ver algo parecido com:

```txt
clima_mysql     0.0.0.0:3307->3306/tcp
airflow_clima   0.0.0.0:8080->8080/tcp
```

---

# 11. Criar a Tabela no MySQL

Entre no container MySQL:

```bash
docker exec -it clima_mysql mysql -uadmin -padmin clima
```

Crie a tabela:

```sql
CREATE TABLE IF NOT EXISTS clima_dados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cidade VARCHAR(100),
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6),
    temperatura DECIMAL(5, 2),
    descricao VARCHAR(255),
    chuva DECIMAL(6, 2),
    data_coleta DATETIME,
    umidade INT,
    nuvens INT
);
```

Confira se a tabela foi criada:

```sql
SHOW TABLES;
```

Saia do MySQL:

```sql
exit;
```

---

# 12. Testar Conexão com MySQL

Crie o arquivo:

```bash
scripts/teste_mysql.py
```

Código:

```python
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

try:
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES;")

    print("✅ Conectado com sucesso ao MySQL!")

    for tabela in cursor.fetchall():
        print("Tabela encontrada:", tabela[0])

    cursor.close()
    conexao.close()

except Exception as erro:
    print("❌ Erro ao conectar no MySQL:", erro)
```

Execute:

```bash
python scripts/teste_mysql.py
```

Resultado esperado:

```txt
✅ Conectado com sucesso ao MySQL!
Tabela encontrada: clima_dados
```

---

# 13. Rodar a Coleta Manualmente

Execute:

```bash
python scripts/coleta_clima.py
```

Resultado esperado:

```txt
Salvo com sucesso: Natal | Temp: ...
Salvo com sucesso: Parnamirim | Temp: ...
Coleta finalizada.
```

---

# 14. Consultar os Dados no MySQL

Entre novamente no MySQL:

```bash
docker exec -it clima_mysql mysql -uadmin -padmin clima
```

Consulte os registros:

```sql
SELECT * FROM clima_dados;
```

Para ver os últimos dados:

```sql
SELECT cidade, temperatura, umidade, nuvens, chuva, data_coleta
FROM clima_dados
ORDER BY data_coleta DESC;
```

---

# 15. Criar DAG do Airflow

Crie o arquivo:

```bash
dags/clima_dag.py
```

Código:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

args_padrao = {
    "owner": "lucio",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="clima_rn_pipeline",
    default_args=args_padrao,
    description="Pipeline de coleta de dados climáticos do RN",
    schedule_interval="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["clima", "rn", "etl", "python"],
) as dag:

    coletar_dados_climaticos = BashOperator(
        task_id="coletar_dados_climaticos",
        bash_command="python /opt/airflow/scripts/coleta_clima.py",
    )

    coletar_dados_climaticos
```

---

# 16. Acessar o Airflow

Abra no navegador:

```txt
http://localhost:8080
```

Login:

```txt
Usuário: admin
Senha: admin
```

Procure a DAG:

```txt
clima_rn_pipeline
```

Ative a DAG e clique em executar.

---

# 17. Problemas Comuns e Soluções

## Erro: Docker não está rodando

Mensagem comum:

```txt
open //./pipe/dockerDesktopLinuxEngine
```

Solução:

1. Abra o Docker Desktop
2. Aguarde iniciar
3. Rode:

```bash
docker ps
```

---

## Erro: conexão recusada no MySQL

Mensagem comum:

```txt
Can't connect to MySQL server on localhost:3307
```

Solução:

```bash
docker ps
```

Se o container não estiver rodando:

```bash
docker compose up -d
```

---

## Erro: API 401

Mensagem comum:

```txt
Invalid API key
```

Solução:

1. Confira a chave no `.env`
2. Gere uma nova chave no OpenWeather
3. Verifique se o código contém:

```python
load_dotenv()
API_KEY = os.getenv("API_KEY")
```

---

## Erro: arquivo não encontrado

Mensagem comum:

```txt
can't open file scripts/coleta_clima.py
```

Solução:

Entre na pasta correta:

```bash
cd Desktop\clima_rn
```

Depois rode:

```bash
python scripts/coleta_clima.py
```

---

## Erro: porta 3306 ocupada

Se a porta 3306 estiver ocupada, use a porta 3307 no `docker-compose.yml`:

```yaml
ports:
  - "3307:3306"
```

E no `.env`:

```env
DB_PORT=3307
```

---

# 18. Checklist Final

Antes de dizer que o projeto está funcionando, confira:

* [ ] Docker Desktop está aberto
* [ ] Container MySQL está rodando
* [ ] Banco `clima` existe
* [ ] Tabela `clima_dados` existe
* [ ] Arquivo `.env` está configurado
* [ ] `requirements.txt` instalado
* [ ] `python scripts/teste_mysql.py` funciona
* [ ] `python scripts/coleta_clima.py` salva dados
* [ ] Airflow abre em `localhost:8080`
* [ ] DAG aparece no Airflow

---

# 19. Como Subir Atualizações para o GitHub

Depois de alterar arquivos:

1. Abra o GitHub Desktop
2. Veja os arquivos modificados
3. Escreva uma mensagem de commit:

```txt
Adiciona guia de execução do projeto
```

4. Clique em:

```txt
Commit to main
```

5. Clique em:

```txt
Push origin
```

---

# 20. Conclusão

Ao concluir este guia, o projeto Clima RN estará executando um pipeline completo de Engenharia de Dados:

```txt
OpenWeather API → Python → MySQL → Airflow → Docker
```

Este projeto demonstra conhecimentos importantes para portfólio, incluindo:

* Consumo de API
* ETL com Python
* Banco de dados MySQL
* Containers com Docker
* Orquestração com Apache Airflow
* Boas práticas com `.env`
* Versionamento com GitHub
