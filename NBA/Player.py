from NBA.PlayerIDMapping import mapAccess

class Player:

    def __init__(self, name):
        try:
            self.playerID = str(mapAccess(name))
            self.playerName = name.title()
        except:
            print("Oops! That's not a valid player.")

    def somthing(self):
        print("f")
