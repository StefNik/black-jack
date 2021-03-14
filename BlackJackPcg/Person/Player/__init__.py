from abc import ABC

from BlackJackPcg.Person import Person


class Player(Person, ABC):

    def __int__(self, user_name):
        super().__init__(user_name=user_name)

    def game_decision(self):
        pass
