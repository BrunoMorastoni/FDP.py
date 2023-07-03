import discord
import gerar_respostas

gerar_respostas.TOKEN_OPENAI = ""



#intents = discord.Intents.default()
intents = discord.Intents().all()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    

    stream = discord.Streaming(name="teste",url="http://example.com")

    await client.change_presence(status=discord.Status.idle,activity=stream)
    
    
    ## Mostrando todos os usuarios do server
    for x in client.get_all_members(): # Atualizar
        print(x)

# decorator my beloved
@client.event
async def on_message(message):

    # porra de loop infinito
    if message.author == client.user:
        return

    # if message.content.startswith('$oi'):
    #     await message.channel.send(message.id)
    #     await message.add_reaction("🤓")
    #     #await message.pin()
    #     await message.reply("halloooo")


    ## Funcao basica de chat
    if message.content.startswith("$$"):
        msg = message.content.strip("$$")

        await message.reply(gerar_respostas.responder(msg))



client.run('')