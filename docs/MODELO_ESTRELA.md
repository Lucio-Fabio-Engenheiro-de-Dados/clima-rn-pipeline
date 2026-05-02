# ⭐ Modelo Estrela — Data Warehouse Clima RN

## 📌 O que é um Modelo Estrela?

O modelo estrela (Star Schema) é uma forma de organizar dados para análise (BI), separando:

- 🔵 Tabela Fato (medidas)
- 🟡 Tabelas Dimensão (contexto)

---

## 🧠 Estrutura do Projeto Clima RN

### 🔵 Tabela Fato

**fato_clima**

Contém os dados numéricos (medidas):

- temperatura
- umidade
- nuvens
- probabilidade_chuva

---

### 🟡 Tabelas Dimensão

#### dim_tempo
- id_tempo (PK)
- data
- dia
- mes
- ano
- hora

#### dim_localizacao
- id_localizacao (PK)
- cidade
- estado
- pais
- latitude
- longitude

#### dim_clima
- id_clima (PK)
- descricao_clima
- nivel_alerta

---

## 🔗 Relacionamento

fato_clima se conecta com:

- dim_tempo
- dim_localizacao
- dim_clima

---

## 🧱 Estrutura Visual


::contentReference[oaicite:0]{index=0}


---

## 💾 SQL Simplificado

```sql
CREATE TABLE dim_tempo (
    id_tempo INT PRIMARY KEY,
    data DATE,
    dia INT,
    mes INT,
    ano INT,
    hora INT  
);

CREATE TABLE dim_localizacao (
    id_localizacao INT PRIMARY KEY,
    cidade VARCHAR(100),
    estado VARCHAR(50),
    pais VARCHAR(50),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6)   
);

CREATE TABLE dim_clima (
    id_clima INT PRIMARY KEY,
    descricao_clima VARCHAR(150),
    nivel_alerta VARCHAR(50)
);

CREATE TABLE fato_clima (
    id INT PRIMARY KEY,
    id_tempo INT,
    id_localizacao INT,
    id_clima INT,
    temperatura DECIMAL(5,2),
    umidade INT,
    nuvens INT,
    probabilidade_chuva DECIMAL(5,2),
    FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id_tempo),
    FOREIGN KEY (id_localizacao) REFERENCES dim_localizacao(id_localizacao),
    FOREIGN KEY (id_clima) REFERENCES dim_clima(id_clima)
);