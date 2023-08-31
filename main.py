import discord
from bot_mantik import sifre_uret

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$password'):
        password = message.content[9:].strip()
        await message.channel.send(sifre_uret(password))
    elif message.content.startswith('$bye'):
        await message.channel.send(":wink:")
    else:
        await message.channel.send(message.content)

client.run("MTE0NDMzMDMwOTQwNDQ1OTA3OQ.GijkXB.NbbSaszvsgmUoHjyqxV37zvAiRiNpAgCqGu5Rs")
