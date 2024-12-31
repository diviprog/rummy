from actors import Player, Bot
from table import Table

class Game:
    def __init__(self, num_players, pvp_or_bots):
        self.num_players = num_players
        self.actors = []
        self.pvp_or_bots = pvp_or_bots

        if self.pvp_or_bots == "pvp":
            for _ in range(self.num_players):
                self.actors.append(Player())
        elif self.pvp_or_bots == "bots":
            self.actors.append(Player())
            for _ in range(self.num_players - 1):
                self.actors.append(Bot())
        
        num_cards = int(input("How many cards do you want to play? (7/10/13) "))
        
        self.table = Table(self.actors, num_cards)