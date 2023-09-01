import discord
import requests
import os
import random
from discord.ext import commands

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix = '$', intents=intents)
world = os.listdir('world')
pluses = os.listdir('pluses')

@bot.command()
async def problems(ctx):
    random_image = random.choice(world)
    with open(f'world/{random_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def pluse(ctx):
    random_image = random.choice(pluses)
    with open(f'pluses/{random_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def questions(ctx):
    await ctx.send("""
1. Что такое изменение климата и почему оно происходит?
2. Откуда в воздухе берется грязь?
3. Какие энергии помогают окружающей среде?

(Чтобы получить ответ на вопрос введи $question 'номер вопроса' )
    """)

@bot.command()
async def question(ctx, number_quest = 0):
    if number_quest == 0:
        await ctx.send('введите номер вопроса, на который вы хотите получить ответ')
    elif number_quest == 1:
        await ctx.send("Изменение климата - это, когда погода меняется из-за газов, которые мы выбрасываем, делая Землю теплее.")
    elif number_quest == 2:
        await ctx.send('Воздух становится грязнее из-за выбросов дыма и грязи от машин и фабрик.')
    elif number_quest == 3:
        await ctx.send('Солнечная и ветровая энергия помогают окружающей среде, потому что они не создают грязь как уголь и нефть.')
    else:
        await ctx.send('Введите после вопроса число от 1-3')

    

bot.run("MTEzNzMxNTEzOTE1OTMzNDk3Mg.GNkIa6.RClEdJxcw_JcKCiYVZI8c0wp6HqfLMzDxfhA-M")

