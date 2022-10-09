from datetime import date
from pprint import pprint
import discord
import random
import wikipedia
import requests
from datetime import datetime


aujourdhui = str(date.today())
valeurs = aujourdhui.split("-")

changement = valeurs [1]

if changement == "01":
    changement = "12"
elif changement == "02":
    changement = "01"
elif changement == "03":
    changement = "02"    
elif changement == "04":
    changement = "03"
elif changement == "05":
    changement = "04"
elif changement == "06":
    changement = "05"
elif changement == "07":
    changement = "06"
elif changement == "08":
    changement = "07"
elif changement == "09":
    changement = "08"
elif changement == "10":
    changement = "09"
elif changement == "11":
    changement = "10"
elif changement == "12":
    changement = "11"



fin = int(str(valeurs[0]) + str(valeurs[1]) + str(valeurs[2]))
debut = int(str(valeurs[0]) + str(changement) + str(valeurs[2]))

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37"

headers = {
    "user-agent": user_agent
}

print(debut)
print (fin)
print(f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Cat/daily/{debut}/{fin}")


# resp = requests.get(f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Cat/daily/{debut}/{fin}", headers=headers)
# # print(resp.content)
# data = resp.json()
# pprint(data['items'][0]['views'])

# header basic_authentification
# header Authorization
# cmd shift j