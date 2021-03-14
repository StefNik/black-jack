from BlackJackPcg.Deck import Deck


class Game:

    def __init__(self, list_players, dealer):
        self.deck = Deck()
        self.list_players = list_players
        self.dealer = dealer

    def initalize_deck(self):
        self.deck.init_deck()

    def shuffle_deck(self):
        self.deck.suffle_deck()

    def give_first_hand_to_participants(self):
        pass
