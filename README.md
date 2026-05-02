# 🌦️ Clima RN – Sistema Inteligente de Monitoramento Climático

Sistema completo de Engenharia de Dados para coleta, processamento e armazenamento de dados climáticos com geração futura de alertas automatizados.

---

## 🚀 Visão Geral

O **Clima RN** é um pipeline de dados que coleta informações meteorológicas em tempo real utilizando API externa, processa os dados e armazena em banco relacional, permitindo análises e geração de alertas.

---
## 📚 Documentação

- 📘 [Dicionário de Dados](docs/DICIONARIO_DADOS.md)

- ⭐ [Modelo Estrela (Data Warehouse)](docs/MODELO_ESTRELA.md)

- 🚨 [Data Mart de Alertas Climáticos](docs/DATA_MART_ALERTAS.md)

---

## 🧠 Arquitetura do Sistema

![Arquitetura do Pipeline Clima RN](docs/arquitetura_clima_rn.png)

### 🔎 Descrição da Arquitetura

O fluxo do sistema segue o padrão moderno de engenharia de dados:

1. **Fonte de Dados**

   * API OpenWeather fornece dados climáticos em tempo real

2. **Camada de Ingestão (Extract)**

   * Script Python realiza requisições HTTP
   * Coleta dados por latitude/longitude

3. **Camada de Processamento (Transform)**

   * Tratamento e padronização dos dados
   * Extração de métricas relevantes:

     * Temperatura
     * Umidade
     * Nuvens
     * Volume de chuva

4. **Camada de Persistência (Load)**

   * Armazenamento em banco MySQL

5. **Orquestração**

   * Apache Airflow executa o pipeline automaticamente

6. **Infraestrutura**

   * Docker gerencia os containers (Airflow + MySQL)

---

## 🔄 Pipeline ETL Detalhado

### 📥 Extração

* Consumo da API OpenWeather
* Uso de coordenadas geográficas
* Requisições HTTP com `requests`

---

### 🔄 Transformação

* Conversão de tipos
* Tratamento de dados ausentes
* Normalização de campos
* Regras de negócio:

  * Se muitas nuvens → possível chuva
  * Se chuva > 0 → alerta

---

### 📤 Carregamento

Inserção no banco:

```sql
clima_dados
```

Campos armazenados:

* cidade
* latitude
* longitude
* temperatura
* descricao
* umidade
* nuvens
* probabilidade_chuva
* data_coleta

---

## ⚙️ Stack Tecnológica

| Camada       | Tecnologia     |
| ------------ | -------------- |
| Linguagem    | Python         |
| Orquestração | Apache Airflow |
| Banco        | MySQL          |
| Container    | Docker         |
| API          | OpenWeather    |

---

## 📂 Estrutura do Projeto

```bash
clima_rn/
│
├── dags/
│   └── clima_dag.py
│
├── scripts/
│   └── coleta_clima.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## 🔐 Segurança

Uso de variáveis de ambiente:

```env
API_KEY=******
DB_HOST=localhost
DB_PORT=3307
DB_USER=admin
DB_PASSWORD=******
DB_NAME=clima
```

✔ Proteção com `.gitignore`
✔ Nenhuma credencial exposta

---

## ▶️ Execução do Projeto

### 1. Clonar

```bash
git clone https://github.com/seu-usuario/clima-rn.git
cd clima-rn
```

---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3. Subir ambiente

```bash
docker compose up -d
```

---

### 4. Executar pipeline manual

```bash
python scripts/coleta_clima.py
```

---

### 5. Airflow

Acesse:

```
http://localhost:8080
```


---

## 📊 Possíveis Expansões

* 📩 Alertas via Telegram
* 📈 Dashboard com Power BI ou Streamlit
* 🤖 Machine Learning para previsão
* 🌎 Escalar para nível nacional

---

## 👨‍💻 Autor

**Lúcio Fábio Barbosa de Lima**
📧 [engenheirodedados.luciofabio@gmail.com](mailto:engenheirodedados.luciofabio@gmail.com)

---

## 🔗 LinkedIn
 
https://www.linkedin.com/in/lucio-fabio-barbosa-de-lima

---

## ⭐ Diferenciais do Projeto

✔ Pipeline ETL completo
✔ Orquestração com Airflow
✔ Uso de Docker
✔ Boas práticas (.env)
✔ Estrutura profissional

---

## 📌 Status

🚧 Em evolução – projeto ativo para portfólio de Engenharia de Dados

## 📘 Guia para iniciantes

Veja o passo a passo completo de como subir o projeto:

👉 [Guia de como subir o projeto](./docs/GUIA_SUBIR_PROJETO.md)
