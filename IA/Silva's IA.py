import os
from groq import Groq

# Defina a chave da API diretamente no código ou garanta que ela esteja configurada corretamente no ambiente
os.environ["GROQ_API_KEY"] = "Digite sua chave API"

client = groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Inicializa a lista de mensagens para manter o contexto da conversa
messages = []

while True:
    usuario = input("Digite uma mensagens ou 'sair' para encerrar: ")

    if usuario.lower() == 'sair':
        print("Conversa encerrada.")
        break

    # Adiciona a mensagem do usuário à lista de mensagens
    messages.append({"role": "user", "content": usuario})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-70b-versatile",
    )

    resposta = chat_completion.choices[0].message.content
    print("Resposta:", resposta)

    # Adiciona a resposta do assistente á lista de mensagens para manter o contexto
    messages.append({"role": "assistant", "content": resposta})