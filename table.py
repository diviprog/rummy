from cards import Deck

class Table:
    def __init__(self, actors, num_cards):
        self.actors = actors
        self.num_cards = num_cards
        self.deck = Deck()

        self.play_round()

    def play_round(self):
        self.distribute_cards()
        for actor in self.actors:
            print(actor.show_cards())
    
    def distribute_cards(self):
        for _ in range(self.num_cards):
            for actor in self.actors:
                actor.get_card(self.deck.choose_card())