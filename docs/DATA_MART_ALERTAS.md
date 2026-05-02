
# 🌧️  DATA MART DE ALERTAS CLIMÁTICOS

## 📌 O que é um Data Mart?

Um Data Mart é um subconjunto de dados focado em uma área específica.

Neste caso: **ALERTAS CLIMÁTICOS**

---

## 🎯 Objetivo

Permitir análises rápidas sobre:

- Riscos climáticos
- Chuvas intensas
- Frequência de alertas
- Cidades mais afetadas

---

## 🧱 Estrutura da Tabela

### tabela: mart_alertas_climaticos

| Campo | Tipo | Descrição |
|---|---|---|
| id | INT | Identificador |
| cidade | VARCHAR | Cidade |
| data | DATE | Data |
| temperatura | DECIMAL | Temperatura |
| umidade | INT | Umidade |
| nuvens | INT | Nuvens |
| probabilidade_chuva | DECIMAL | Chance de chuva |
| nivel_alerta | VARCHAR | Nível do alerta |

---

## 💾 SQL

```sql
CREATE TABLE mart_alertas_climaticos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cidade VARCHAR(100),
    data DATE,
    temperatura DECIMAL(5,2),
    umidade INT,
    nuvens INT,
    probabilidade_chuva DECIMAL(5,2),
    nivel_alerta VARCHAR(50)
);
````

---

## 🔄 Processo ETL

```text
clima_dados (fonte)
        ↓
filtro: nivel_alerta IN ('ALERTA', 'RISCO ALTO')
        ↓
mart_alertas_climaticos
```

---

## 📊 Consultas úteis

### Cidades com mais alertas

```sql
SELECT cidade, COUNT(*) AS total_alertas
FROM mart_alertas_climaticos
GROUP BY cidade
ORDER BY total_alertas DESC;
```

---

### Média de chuva por cidade

```sql
SELECT cidade, AVG(probabilidade_chuva)
FROM mart_alertas_climaticos
GROUP BY cidade;
```

---

## 🚀 Benefícios

* Análise rápida
* Foco em decisão
* Ideal para dashboards
* Estrutura de empresa real

---





