import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="admin",
        password="admin",
        database="clima"
    )

    print("✅ Conectado com sucesso ao MySQL!")

    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES;")

    for tabela in cursor:
        print("Tabela encontrada:", tabela[0])

    cursor.close()
    conexao.close()

except Exception as e:
    print("❌ Erro ao conectar:", e)     