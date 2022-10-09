from enum import auto
import discord
import random
import wikipedia

TOKEN = "MTAyODQ4MDI0NTQwMzIyNjExNA.GQSlNB.hemhaKRWJK2ipxDVE2WYu_leMq-NE1ao-zZD9M"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("connecte comme {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message}({channel})")

    if message.author == client.user:
        return  


    if message.channel.name == "fr" or "test-bot" or "general":
        if user_message.lower() == "ping" :
            await message.channel.send(f"pong")
            return  
        if user_message.lower() == "!lance un dé" :
            reponse = f" ton résultat est "
            await message.channel.send(reponse)
            await message.channel.send(f"{random.randrange(1,6)}")
            return     
        if user_message.lower() == "non" :
            await message.channel.send(f"bril")
            return              
        if user_message.lower() == "oui" :
            await message.channel.send(f"stiti")
            return 
        if user_message.lower() == "quoi" :
            await message.channel.send(f"feur")
            return 
        if user_message.lower() == "allo" :
            await message.channel.send(f"à l'huile")
            return 

        if user_message.lower().startswith("!résumé/"):
            commande = user_message.lower()
            nomArticle = commande.split("/")
            wikipedia.set_lang(nomArticle[1])
            await message.channel.send(f"{wikipedia.summary(nomArticle[2], sentences = 2, auto_suggest = False)})")  
            return
        # if message.author.id == 696776064113836112:
        #     words = ["Fanny", "Murielle", "Krystel", "Sarah", "Mattie"]
        #     await message.channel.send(f"raph aime {random.choice(words)}")
        #     return
client.run(TOKEN)