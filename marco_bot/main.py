from datetime import date
from pprint import pprint
import discord
import random
import wikipedia
import requests
from datetime import datetime

TOKEN = "your_token_here"

client = discord.Client(intents=discord.Intents.all())

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37"

headers = {
    "user-agent": user_agent
}


aujourdhui = str(date.today())
valeurs = aujourdhui.split("-")

changement = valeurs [1]

if changement == "01":
    changement = "11"
elif changement == "02":
    changement = "12"
elif changement == "03":
    changement = "01"    
elif changement == "04":
    changement = "02"
elif changement == "05":
    changement = "03"
elif changement == "06":
    changement = "04"
elif changement == "07":
    changement = "05"
elif changement == "08":
    changement = "06"
elif changement == "09":
    changement = "07"
elif changement == "10":
    changement = "08"
elif changement == "11":
    changement = "09"
elif changement == "12":
    changement = "10"



fin = int(str(valeurs[0]) + str(valeurs[1]) + str(valeurs[2]))
debut = int(str(valeurs[0]) + str(changement) + str(valeurs[2]))

with open("animals.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split("\n")))
  
    # print random string
    #print(random.choice(words))

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
        if user_message.lower() == "ping":
            await message.channel.send(f"pong")
            return  
        elif user_message.lower() == "!lance un d??" :
            reponse = f" ton r??sultat est "
            await message.channel.send(reponse)
            await message.channel.send(f"{random.randrange(1,6)}")
            return     
        elif user_message.lower() == "non" or user_message.endswith("non"):
            await message.channel.send(f"bril")
            return              
        elif user_message.lower() == "oui" or user_message.endswith("oui") :
            await message.channel.send(f"stiti")
            return 
        elif user_message.lower() == "quoi" or user_message.endswith("quoi") or user_message.endswith("quoi?") or user_message.endswith("quoi ?"):
            await message.channel.send(f"feur")
            return 
        elif user_message.lower() == "allo" :
            await message.channel.send(f"?? l'huile")
            return 

        elif user_message.lower().startswith("!r??sum??/"):
            commande = user_message.lower()
            nomArticle = commande.split("/")
            wikipedia.set_lang(nomArticle[1])
            await message.channel.send(f"{wikipedia.summary(nomArticle[2], sentences = 2, auto_suggest = False)}")  
            return

        elif user_message.startswith("!views/"):
            articleNom = user_message.split("/")
            wikipage = articleNom[1]
            resp = requests.get(f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{wikipage}/monthly/{debut}/{fin}", headers=headers)
            # print(resp.content)
            print (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{wikipage}/monthly/{debut}/{fin}")
            data = resp.json()
            await message.channel.send(f"Cette page wikipedia a eu {(data['items'][0]['views'])} vues durant le dernier mois")  
            return


#todo enleverl les espaces


        elif user_message.lower() == "!jeu wikipedia":
            x = random.choice(words)
            y = random.choice(words)
            await message.channel.send(f"Quelle est la page entre {random.choice(words)} et {random.choice(words)} qui a eu le plus de visites lors du denier mois ?")
            resp = requests.get(f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{x}/monthly/{debut}/{fin}", headers=headers)
            data = resp.json()
            x1 = (data['items'][0]['views'])

            resp = requests.get(f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{y}/monthly/{debut}/{fin}", headers=headers)
            data = resp.json()
            y1 = (data['items'][0]['views'])
            
            if user_message == x :
                if x1<y1:
                     await message.channel.send("nuuul")
                if x1>y1:
                    await message.channel.send("bien ouej")

            if user_message == y :
                if x1<y1:
                     await message.channel.send("bien ouej")
                if x1>y1:
                    await message.channel.send("nuuul")

        # if message.author.id == 696776064113836112:
        #     words = ["Fanny", "Murielle", "Krystel", "Sarah", "Mattie"]
        #     await message.channel.send(f"raph aime {random.choice(words)}")
        #     return
client.run(TOKEN)