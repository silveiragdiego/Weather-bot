import discord
import requests #biblioteca que realiza requisições
from discord.ext import commands
import pyttsx3 #biblioteca de síntese de fala

engine = pyttsx3.init() #criador do objeto de síntese de fala

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def get_weather(city: str)-> str:
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return("Não foi possível obter os dados metereológicos :(")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a weather bot {bot.user}!')

@bot.command()
async def weather(ctx,*,city: str):
    weather_info = get_weather(city)
    await ctx.send(f"O tempo em {city}: {weather_info}")
    speak(weather_info)

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

bot.run("")

