# 📘 Dicionário de Dados — Projeto Clima RN

## 🌧️ Projeto: Clima RN

O **Clima RN** é um projeto de Engenharia de Dados voltado para o monitoramento climático automatizado de cidades do Rio Grande do Norte.

O sistema coleta dados climáticos de uma API externa, transforma essas informações, armazena os resultados em arquivos `.CSV`, `.XLSX` e banco de dados MySQL, além de permitir o envio de alertas automáticos via Telegram.

---

# 1. O que é um Dicionário de Dados?

Um **Dicionário de Dados** é um documento que explica a estrutura dos dados utilizados em um sistema.

Ele funciona como um “manual do banco de dados”, ajudando a entender:

- O nome das tabelas;
- O significado de cada coluna;
- O tipo de dado armazenado;
- Se o campo é obrigatório;
- Quais campos são chaves primárias ou estrangeiras;
- Quais regras de negócio estão associadas aos dados.

Em projetos de Engenharia de Dados, o dicionário de dados é importante porque melhora a organização, facilita a manutenção e deixa o projeto mais profissional.

---

# 2. Visão Geral dos Dados

No projeto Clima RN, os dados principais representam informações climáticas coletadas periodicamente para diferentes cidades.

Exemplos de dados coletados:

- Cidade;
- Estado;
- País;
- Temperatura;
- Sensação térmica;
- Umidade;
- Percentual de nuvens;
- Velocidade do vento;
- Condição climática;
- Probabilidade de chuva;
- Data e hora da coleta.

---

# 3. Tabela Principal: clima_dados

A tabela `clima_dados` armazena os dados climáticos coletados pela aplicação.

## Descrição

Tabela responsável por armazenar os registros climáticos coletados automaticamente pelo sistema Clima RN.

Cada linha representa uma coleta de clima feita para uma determinada cidade em uma determinada data e hora.

---

# 4. Estrutura da Tabela clima_dados

| Campo               | Tipo de Dado  | Obrigatório | Chave | Descrição                                       |
| ------------------- | ------------- | ----------- | ----- | ----------------------------------------------- |
| id                  | INT           | Sim         | PK    | Identificador único de cada registro climático. |
| cidade              | VARCHAR(100)  | Sim         |       | Nome da cidade monitorada.                      |
| estado              | VARCHAR(50)   | Sim         |       | Estado da cidade monitorada.                    |
| pais                | VARCHAR(50)   | Sim         |       | País da cidade monitorada.                      |
| latitude            | DECIMAL(10,6) | Não         |       | Latitude da cidade consultada.                  |
| longitude           | DECIMAL(10,6) | Não         |       | Longitude da cidade consultada.                 |
| temperatura         | DECIMAL(5,2)  | Sim         |       | Temperatura atual em graus Celsius.             |
| sensacao_termica    | DECIMAL(5,2)  | Não         |       | Temperatura percebida pelo corpo humano.        |
| temperatura_minima  | DECIMAL(5,2)  | Não         |       | Temperatura mínima prevista ou registrada.      |
| temperatura_maxima  | DECIMAL(5,2)  | Não         |       | Temperatura máxima prevista ou registrada.      |
| umidade             | INT           | Sim         |       | Percentual de umidade relativa do ar.           |
| nuvens              | INT           | Sim         |       | Percentual de cobertura de nuvens.              |
| velocidade_vento    | DECIMAL(5,2)  | Não         |       | Velocidade do vento.                            |
| descricao_clima     | VARCHAR(150)  | Sim         |       | Descrição textual da condição climática.        |
| probabilidade_chuva | DECIMAL(5,2)  | Não         |       | Probabilidade estimada de chuva.                |
| nivel_alerta        | VARCHAR(50)   | Não         |       | Classificação do nível de alerta climático.     |
| data_coleta         | DATETIME      | Sim         |       | Data e hora em que os dados foram coletados.    |
| fonte_dados         | VARCHAR(100)  | Não         |       | Origem dos dados, como OpenWeather API.         |

---

# 5. Explicação Campo por Campo

## id

Identificador único de cada registro.

Exemplo:

```text
1
2
3
```

Esse campo serve para diferenciar cada linha da tabela.

---

## cidade

Nome da cidade monitorada.

Exemplo:

```text
Natal
Mossoró
Caicó
Parnamirim
```

Esse campo permite saber de qual cidade os dados climáticos foram coletados.

---

## estado

Nome ou sigla do estado.

Exemplo:

```text
RN
Rio Grande do Norte
```

No projeto Clima RN, o estado principal será o Rio Grande do Norte.

---

## pais

Nome ou sigla do país.

Exemplo:

```text
BR
Brasil
```

Esse campo é útil caso o projeto seja expandido para outras regiões ou países.

---

## latitude

Coordenada geográfica da cidade.

Exemplo:

```text
-5.7945
```

A latitude ajuda a localizar a cidade com maior precisão.

---

## longitude

Coordenada geográfica da cidade.

Exemplo:

```text
-35.2110
```

A longitude, junto com a latitude, permite consultar dados climáticos por coordenadas.

---

## temperatura

Temperatura atual no momento da coleta.

Exemplo:

```text
28.50
```

Normalmente armazenada em graus Celsius.

---

## sensacao_termica

Temperatura percebida pelo corpo humano.

Exemplo:

```text
31.20
```

Pode ser diferente da temperatura real devido à umidade, vento e radiação solar.

---

## temperatura_minima

Menor temperatura prevista ou registrada.

Exemplo:

```text
24.00
```

---

## temperatura_maxima

Maior temperatura prevista ou registrada.

Exemplo:

```text
33.00
```

---

## umidade

Percentual de umidade relativa do ar.

Exemplo:

```text
82
```

Valores altos de umidade podem indicar maior possibilidade de chuva.

---

## nuvens

Percentual de cobertura de nuvens.

Exemplo:

```text
90
```

Quanto maior o percentual de nuvens, maior pode ser a chance de tempo fechado ou chuva.

---

## velocidade_vento

Velocidade do vento no momento da coleta.

Exemplo:

```text
4.50
```

Pode ser usada para análises climáticas e alertas de condições severas.

---

## descricao_clima

Descrição textual do clima retornada pela API.

Exemplo:

```text
céu limpo
nublado
chuva leve
chuva moderada
trovoadas
```

Esse campo facilita a leitura humana dos dados.

---

## probabilidade_chuva

Percentual estimado de possibilidade de chuva.

Exemplo:

```text
75.00
```

No projeto Clima RN, esse campo pode ser calculado com base em fatores como:

* Umidade;
* Percentual de nuvens;
* Descrição climática;
* Previsão retornada pela API.

---

## nivel_alerta

Classificação do risco climático.

Exemplo:

```text
NORMAL
ATENÇÃO
ALERTA
RISCO ALTO
```

Esse campo pode ser usado para disparar mensagens automáticas pelo Telegram.

---

## data_coleta

Data e hora em que a coleta foi realizada.

Exemplo:

```text
2026-05-02 08:30:00
```

Esse campo é essencial para análises históricas.

---

## fonte_dados

Origem dos dados climáticos.

Exemplo:

```text
OpenWeather API
```

Esse campo ajuda a identificar de onde os dados vieram.

---

# 6. Código SQL para Criar a Tabela

```sql
CREATE DATABASE IF NOT EXISTS clima;

USE clima;

CREATE TABLE IF NOT EXISTS clima_dados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    temperatura DECIMAL(5,2) NOT NULL,
    sensacao_termica DECIMAL(5,2),
    temperatura_minima DECIMAL(5,2),
    temperatura_maxima DECIMAL(5,2),
    umidade INT NOT NULL,
    nuvens INT NOT NULL,
    velocidade_vento DECIMAL(5,2),
    descricao_clima VARCHAR(150) NOT NULL,
    probabilidade_chuva DECIMAL(5,2),
    nivel_alerta VARCHAR(50),
    data_coleta DATETIME NOT NULL,
    fonte_dados VARCHAR(100)
);
```

---

# 7. Exemplo de Registro

| id | cidade | estado | pais   | temperatura | umidade | nuvens | descricao_clima | probabilidade_chuva | nivel_alerta | data_coleta         |
| -- | ------ | ------ | ------ | ----------- | ------- | ------ | --------------- | ------------------- | ------------ | ------------------- |
| 1  | Natal  | RN     | Brasil | 28.50       | 82      | 90     | nublado         | 75.00               | ATENÇÃO      | 2026-05-02 08:30:00 |

---

# 8. Exemplo de INSERT

```sql
INSERT INTO clima_dados (
    cidade,
    estado,
    pais,
    latitude,
    longitude,
    temperatura,
    sensacao_termica,
    temperatura_minima,
    temperatura_maxima,
    umidade,
    nuvens,
    velocidade_vento,
    descricao_clima,
    probabilidade_chuva,
    nivel_alerta,
    data_coleta,
    fonte_dados
) VALUES (
    'Natal',
    'RN',
    'Brasil',
    -5.7945,
    -35.2110,
    28.50,
    31.20,
    24.00,
    33.00,
    82,
    90,
    4.50,
    'nublado',
    75.00,
    'ATENÇÃO',
    NOW(),
    'OpenWeather API'
);
```

---

# 9. Regras de Negócio

## Regra 1 — Probabilidade de chuva

A probabilidade de chuva pode ser estimada considerando:

* Umidade alta;
* Grande cobertura de nuvens;
* Descrição climática indicando chuva ou tempo nublado.

Exemplo de regra simples:

```text
Se umidade >= 80 e nuvens >= 70, então existe possibilidade de chuva.
```

---

## Regra 2 — Nível de alerta

Sugestão de classificação:

| Condição                             | Nível de Alerta |
| ------------------------------------ | --------------- |
| Probabilidade de chuva menor que 40% | NORMAL          |
| Probabilidade entre 40% e 69%        | ATENÇÃO         |
| Probabilidade entre 70% e 89%        | ALERTA          |
| Probabilidade igual ou maior que 90% | RISCO ALTO      |

---

## Regra 3 — Envio de alerta Telegram

O sistema pode enviar alerta quando:

```text
nivel_alerta = 'ALERTA'
```

ou

```text
nivel_alerta = 'RISCO ALTO'
```

---

# 10. Exemplo de Consulta SQL

## Ver todos os dados

```sql
SELECT *
FROM clima_dados;
```

---

## Ver dados apenas de Natal

```sql
SELECT *
FROM clima_dados
WHERE cidade = 'Natal';
```

---

## Ver cidades com alerta

```sql
SELECT 
    cidade,
    temperatura,
    umidade,
    nuvens,
    probabilidade_chuva,
    nivel_alerta,
    data_coleta
FROM clima_dados
WHERE nivel_alerta IN ('ALERTA', 'RISCO ALTO');
```

---

## Média de temperatura por cidade

```sql
SELECT 
    cidade,
    AVG(temperatura) AS media_temperatura
FROM clima_dados
GROUP BY cidade;
```

---

## Média de umidade por cidade

```sql
SELECT 
    cidade,
    AVG(umidade) AS media_umidade
FROM clima_dados
GROUP BY cidade;
```

---

## Quantidade de coletas por cidade

```sql
SELECT 
    cidade,
    COUNT(*) AS total_coletas
FROM clima_dados
GROUP BY cidade;
```

---

# 11. Relação com Engenharia de Dados

Este dicionário de dados ajuda a documentar a etapa de armazenamento do pipeline.

No projeto Clima RN, o fluxo de dados pode ser entendido assim:

```text
API OpenWeather
        ↓
Extract
        ↓
Transform
        ↓
Load
        ↓
CSV / Excel / MySQL
        ↓
Alertas Telegram
        ↓
Análises e Dashboards
```

---

# 12. Benefícios do Dicionário de Dados no Projeto

Este documento ajuda a:

* Organizar melhor o banco de dados;
* Facilitar a manutenção do projeto;
* Ajudar outras pessoas a entenderem o sistema;
* Melhorar a apresentação no GitHub;
* Demonstrar boas práticas de Engenharia de Dados;
* Mostrar preocupação com documentação técnica.

---

# 13. Próximas Melhorias

Algumas melhorias futuras para o projeto:

* Criar tabela separada para cidades;
* Criar tabela separada para alertas;
* Criar histórico de envio de mensagens Telegram;
* Criar dashboard com Power BI, Streamlit ou Metabase;
* Criar modelo estrela para análise climática;
* Criar Data Mart de alertas climáticos.

---

# 14. Versão do Documento

| Informação | Valor                                        |
| ---------- | -------------------------------------------- |
| Projeto    | Clima RN                                     |
| Documento  | Dicionário de Dados                          |
| Versão     | 1.0                                          |
| Autor      | Lúcio Fábio Barbosa de Lima                  |
| Área       | Engenharia de Dados                          |
| Finalidade | Documentação técnica para GitHub e portfólio |


---


