import json
import requests
#import org.json

def mapGen():
    """Run only to re-generate NameIDMapping.json"""
    url = 'http://stats.nba.com/stats/commonallplayers/?leagueid=00&season=2017-18&IsOnlyCurrentSeason=1'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    headers = {'User-Agent': user_agent}
    request = requests.get(url=url, headers=headers, timeout=3)
    players_json = request.json()
    #JSONObject
    player_dict = {}
    with open('../NameIDMapping.json', 'w') as output:
        for player in players_json['resultSets'][0]['rowSet']:
            player_dict[player[2]] = player[0]
        output.write(json.dumps(player_dict, sort_keys=True, indent=4, separators=(',', ': ')))

def mapAccess(playerName):
    """Retrieve PlayerID from NameIDMapping.json
    using players full name.
    mapAccess('Kevin Durant') --> 201142"""
    with open('../NameIDMapping.json', 'r') as f:
        mapping = json.load(f)
        try:
            return mapping[playerName.title()]
        except KeyError as e:
            print(playerName.title() + " is not a player that exists.")
            raise e
            #raise ValueError(playerName + " is not a player that exists.")

mapGen()
#mapAccess("kevin durant")