class Actor:
    def __init__(self):
        self.cards = []
    
    def get_card(self, card):
        self.cards.append(card)

    def show_cards(self):
        return [card.show() for card in self.cards]
    
class Player(Actor):
    def __init__(self):
        super().__init__()
        self.id = "player"

class Bot(Actor):
    def __init__(self):
        super().__init__()
        self.id = "bot"