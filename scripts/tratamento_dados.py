import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="admin",
        password="admin",
        database="clima"
    )

def classificar_condicao(descricao, chuva, umidade, nuvens):
    descricao = (descricao or "").lower()
    chuva = float(chuva or 0)
    umidade = int(umidade or 0)
    nuvens = int(nuvens or 0)

    # 1. Chuva real observada
    if chuva >= 10:
        return "ALERTA FORTE DE CHUVA"
    elif chuva >= 5:
        return "ALERTA MODERADO DE CHUVA"
    elif chuva > 0:
        return "CHUVA LEVE"

    # 2. Possibilidade muito alta baseada em indicadores
    if (
        umidade >= 85 and
        nuvens >= 85 and
        any(termo in descricao for termo in ["nublado", "encoberto", "muitas nuvens"])
    ):
        return "ALTA POSSIBILIDADE DE CHUVA"

    # 3. Possibilidade moderada
    if (
        umidade >= 70 and
        nuvens >= 60
    ):
        return "POSSIBILIDADE DE CHUVA"

    # 4. Apenas céu com nuvens, mas sem muitos indicadores
    if any(termo in descricao for termo in [
        "nublado",
        "nuvens dispersas",
        "nuvens quebradas",
        "muitas nuvens",
        "encoberto"
    ]):
        return "TEMPO NUBLADO"

    return "SEM CHUVA"

def gerar_mensagem_teste_completa():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT cidade, temperatura, descricao, chuva, umidade, nuvens, data_coleta
        FROM clima_dados
        WHERE DATE(data_coleta) = CURDATE()
        ORDER BY cidade, data_coleta DESC
    """

    cursor.execute(query)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    if not resultados:
        return "Nenhum dado climático encontrado para hoje."

    ultimos_por_cidade = {}
    for linha in resultados:
        cidade = linha["cidade"]
        if cidade not in ultimos_por_cidade:
            ultimos_por_cidade[cidade] = linha

    mensagem = "🌦️ Relatório climático diário - Clima RN\n\n"

    for cidade, dados in ultimos_por_cidade.items():
        nivel = classificar_condicao(
            dados["descricao"],
            dados["chuva"],
            dados["umidade"],
            dados["nuvens"]
        )

        chuva = float(dados["chuva"] or 0)
        umidade = int(dados["umidade"] or 0)
        nuvens = int(dados["nuvens"] or 0)

        mensagem += (
            f"{nivel} - {cidade}\n"
            f"Temperatura: {dados['temperatura']}°C\n"
            f"Clima: {dados['descricao']}\n"
            f"Chuva na última hora: {chuva} mm\n"
            f"Umidade: {umidade}%\n"
            f"Nuvens: {nuvens}%\n\n"
        )

    return mensagem

def gerar_mensagem_alerta():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT cidade, temperatura, descricao, chuva, umidade, nuvens, data_coleta
        FROM clima_dados
        WHERE DATE(data_coleta) = CURDATE()
        ORDER BY cidade, data_coleta DESC
    """

    cursor.execute(query)
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    if not resultados:
        return "Nenhum dado climático encontrado para hoje."

    ultimos_por_cidade = {}
    for linha in resultados:
        cidade = linha["cidade"]
        if cidade not in ultimos_por_cidade:
            ultimos_por_cidade[cidade] = linha

    linhas_alerta = []

    for cidade, dados in ultimos_por_cidade.items():
        nivel = classificar_condicao(
            dados["descricao"],
            dados["chuva"],
            dados["umidade"],
            dados["nuvens"]
        )

        if nivel != "SEM CHUVA":
            chuva = float(dados["chuva"] or 0)
            umidade = int(dados["umidade"] or 0)
            nuvens = int(dados["nuvens"] or 0)

            linhas_alerta.append(
                f"{nivel} - {cidade}\n"
                f"Temperatura: {dados['temperatura']}°C\n"
                f"Clima: {dados['descricao']}\n"
                f"Chuva na última hora: {chuva} mm\n"
                f"Umidade: {umidade}%\n"
                f"Nuvens: {nuvens}%\n"
            )

    if not linhas_alerta:
        return "Sem alerta de chuva para as cidades monitoradas hoje."

    mensagem = "🌧️ Alerta climático diário - Clima RN\n\n"
    mensagem += "\n".join(linhas_alerta)

    return mensagem

if __name__ == "__main__":
    print(gerar_mensagem_teste_completa())