import json

def mapGen():
    """Run only to re-generate NameIDMapping.json"""
    with open('Players.json','r') as f:
        players_dict = json.load(f)
        playerDict = {}
        for player in players_dict['resultSets'][0]['rowSet']:
            playerDict[player[2]] = player[0]
        output = open('NameIDMapping.json', 'w')
        output.write(json.dumps(playerDict))

def mapAccess(playerName):
    """Retrieve PlayerID from NameIDMapping.json
    using players full name.
    mapAccess('Kevin Durant') --> 201142"""
    with open('NameIDMapping.json', 'r') as f:
        mapping = json.load(f)
        if playerName.title() not in mapping:
            raise ValueError(playerName + " is not a player that exists.")
        return mapping[playerName.title()]