import discord
from discord.ext import commands
import gerador_respostas
import time
gerador_respostas.TOKEN_OPENAI = ""

intents = discord.Intents.all()

intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.listen()
async def on_ready():
    print(f"{bot.user} ON")

    atividade = discord.Streaming(name="Davos_AI",url="https://www.twitch.tv/bruno_giradas")
    await bot.change_presence(activity=atividade,status=discord.Status.idle)



### Configurando para o bot entrar e sair do canal


@bot.command(name="f")
async def rsp(ctx, *args):
    pergunta = ' '.join(args)
    await ctx.message.add_reaction("✅")
    #resposta = pergunta
    resposta = gerador_respostas.gerar_resposta_texto(pergunta)
    
    if ctx.author.voice:
        gerador_respostas.gerar_tts(resposta)

        ## Bot ja conectado ?
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice_client:
            time.sleep(1)
            ctx.voice_client.play(discord.FFmpegPCMAudio(executable="simulado/ffplayer/ffmpeg",source='audios/tts_audio.mp3'))
            await ctx.reply(resposta)
            return
        else:
            channel = ctx.author.voice.channel
            vc = await channel.connect()

    else:
        await ctx.reply(resposta)


@bot.command(name="p")
@commands.cooldown(1, 25, commands.BucketType.user)
async def responder_imagem(ctx, *args):
    pergunta = ' '.join(args)
    await ctx.message.add_reaction("✅")
    resposta = gerador_respostas.gerar_resposta_imagem(pergunta)
    
    await ctx.send(resposta)


## Abandonado
# @bot.command()
# @commands.cooldown(1, 5, commands.BucketType.user)
# async def wl(ctx):
#     usuario = str(ctx.author)
#     if usuario in white_list:
#         return
#     else:
#         await ctx.message.add_reaction("✅")
#         await ctx.message.add_reaction("❌")


# Tratando coolddown dos comandos
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        await ctx.message.add_reaction("❌")




## Mesmas funcoes do discord client
# @bot.listen()
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     #await message.reply("hallo")



bot.run("")
