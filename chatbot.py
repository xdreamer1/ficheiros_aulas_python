# Importa a classe OpenAI da biblioteca openai
from openai import OpenAI
 
# Importa a função load_dotenv para ler o ficheiro .env
from dotenv import load_dotenv
 
# Importa o módulo os para aceder às variáveis de ambiente
import os
 
# Carrega as variáveis guardadas no ficheiro .env
load_dotenv()
 
# Cria o cliente OpenAI usando a chave guardada na variável de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
 
# Define a função enviar_mensagem
# Recebe a mensagem do utilizador e o histórico da conversa
def enviar_mensagem(mensagem, lista_mensagens=None):
 
    # Verifica se a lista está vazia
    # Se estiver, cria uma nova lista
    if lista_mensagens is None:
        lista_mensagens = []
 
    # Adiciona a mensagem do utilizador ao histórico
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
 
    # Envia a conversa para a API da OpenAI
    resposta = client.chat.completions.create(
        model="gpt-6-luna",
        messages=lista_mensagens
    )
 
    # Devolve a resposta do chatbot
    return resposta.choices[0].message
 
# Cria a lista para guardar o histórico
lista_mensagens = []
 
# Mantém o chatbot em execução
while True:
 
    # Pede ao utilizador para escrever uma mensagem
    texto = input("Escreva aqui sua mensagem: ")
 
    # Fecha o programa se escrever "sair"
    if texto.lower() == "sair":
        break
 
    else:
        # Envia a mensagem e recebe a resposta
        resposta = enviar_mensagem(texto, lista_mensagens)
 
        # Guarda a resposta no histórico
        lista_mensagens.append({
            "role": "assistant",
            "content": resposta.content
        })
 
        # Mostra a resposta
        print("Chatbot:", resposta.content)