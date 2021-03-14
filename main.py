from BlackJackPcg.Game import Game
from BlackJackPcg.Person.Dealer import Dealer
from BlackJackPcg.Person.Player import Player


if __name__ == '__main__':
    delear = Dealer()
    player1 = Player("user1")

    game = Game([player1], delear)

    game.initalize_deck()
    game.shuffle_deck()
    game.give_first_hand_to_participants()




