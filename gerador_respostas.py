import openai
import time
import requests 
import urllib.request
import re
import unidecode
TOKEN_OPENAI = ""
TOKEN_GROUP_OPENAI = ""


# Gambiarra da ai

msgUsr = "mensagem do usuario:"
texto1 = "Responda ao usuário levando como base o próximo texto "
texto2 = "Seu nome e davos"


def gerar_resposta_imagem(input_imagem) -> str:
    openai.api_key = TOKEN_OPENAI
    response = openai.Image.create(
    prompt=input_imagem,
    n=2,
    size="256x256"
    )

    return response["data"][0]["url"]



def gerar_resposta_texto(pergunta) -> str:
    pergunta = texto1 + texto2 + msgUsr + pergunta
    print(pergunta)
    openai.api_key = TOKEN_OPENAI

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=pergunta,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response['choices'][0]['text']

def gerar_tts(texto) -> None:
    
    texto = texto.replace(" ","%20")
    texto = re.sub("\s","",texto)
    texto_sem_acento = unidecode.unidecode(texto)
    tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&client=tw-ob&tl=pt-BR&q={texto_sem_acento}"
    nome_arquivo = "audios/tts_audio.mp3"
    urllib.request.urlretrieve(tts_url, nome_arquivo)

    return 0



if __name__ == "__main__":
    print("dentro do modulo")
