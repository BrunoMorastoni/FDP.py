import openai
import time


TOKEN_OPENAI = ""
TOKEN_GROUP_OPENAI = ""


# Gambiarra da ai

msgUsr = "mensagem do usuario:"
texto1 = "Responda ao usuário levando como base o próximo texto "
texto2 = "O Seu nome e davos. "



def responder(pergunta) -> str:
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
    resposta = response['choices'][0]['text']

    return resposta


if __name__ == "__main__":
    print("dentro do modulo")