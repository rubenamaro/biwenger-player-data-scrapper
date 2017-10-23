import urllib.request
import json
import time
from pprint import pprint

URL_PLAYERS = 'https://biwenger.as.com/api/v1/players/la-liga?limit=500&sort=-id,-points,-price'
HEADERS = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOjI1NzI1MTc1LCJpYXQiOjE1MDM5MzQ1NzZ9.uD4mkLR3jPijO7JDiozP9GZJZ-Vtf4HSN1cFzLJ0ztA',
    'x-league': '516802'
}
start_time = time.time()
players_url = URL_PLAYERS

reqPlayers = urllib.request.Request(
    players_url,
    data=None,
    headers= HEADERS
)

fPlayers = urllib.request.urlopen(reqPlayers)
responsePlayers = fPlayers.read().decode('utf-8')

dataPlayers = json.loads(responsePlayers)

for item in dataPlayers['data']:
    if item['id'] == 10746:
        player = item
        break

player = str(player).replace("'", '"')
print(player)
print("--- %s seconds ---" % (time.time() - start_time))