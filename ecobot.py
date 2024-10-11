import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bienvenido a la prueba de reciclaje {bot.user}')

@bot.command()
async def colores(ctx):
    await ctx.send(f"Verde: residuos orgánicos, Azul: papel y cartón, Amarillo: plásticos y latas, Rojo: residuos peligrosos, Gris:residuos no reciclables, Blanco:vidrio")

@bot.command()
async def reciclaje(ctx):
    await ctx.send(f'Reciclar es clave para cuidar el planeta, ya que reduce la cantidad de basura que termina en vertederos y ayuda a disminuir la contaminación. Al reutilizar materiales como plástico, vidrio y papel, se ahorra energía y recursos naturales, como el agua y los árboles. Además, reciclar disminuye la emisión de gases de efecto invernadero, contribuyendo a frenar el cambio climático. Al hacerlo, participas activamente en la creación de un futuro más limpio y sostenible. También incentiva la creatividad y fomenta hábitos responsables en la vida diaria. ¡Es una manera sencilla de marcar una gran diferencia!')

@bot.command()
async def contaminación(ctx):
    await ctx.send(f'La contaminación es peligrosa porque daña el aire que respiramos, lo que puede causar enfermedades respiratorias y afectar nuestra salud. También contamina el agua, haciéndola insegura para beber y dañando la vida marina. Además, destruye ecosistemas, lo que amenaza la supervivencia de animales y plantas. La acumulación de basura y químicos tóxicos contamina suelos, lo que afecta la agricultura y la producción de alimentos. La contaminación contribuye al calentamiento global, provocando fenómenos extremos como inundaciones o sequías. Si no actuamos, el impacto será mayor en el futuro, afectando a las próximas generaciones.')

@bot.command()
async def ideas(ctx):
    await ctx.send(f"https://www.youtube.com/watch?v=KRkyZ466zA4")

@bot.command()
async def consejos(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=nvUqnpicSd0')

@bot.command()
async def olvidado(ctx):
    await ctx.send(f"https://www.youtube.com/watch?v=21abiu5ftMQ")
    
@bot.command()
async def world(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=499GB-HJcbc')
