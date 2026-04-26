import requests
from tratamento_dados import gerar_mensagem_alerta

TOKEN = "SEU_TOKEN_DO_BOT"
CHAT_ID = "SEU_CHAT_ID"

def enviar_telegram():
    mensagem = gerar_mensagem_alerta()

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }

    resposta = requests.post(url, data=payload, timeout=30)

    if resposta.status_code == 200:
        print("Mensagem enviada com sucesso no Telegram.")
    else:
        print("Erro ao enviar mensagem no Telegram.")
        print(resposta.text)

if __name__ == "__main__":
    enviar_telegram()