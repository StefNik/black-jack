from abc import ABC

from BlackJackPcg.Person import Person


class Dealer(Person, ABC):

    def __int__(self):
        super().__init__(user_name="Dealer")

    def game_decision(self):
        pass

    def show_hand_in_users_turn(self):
        pass
