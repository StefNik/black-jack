
from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, user_name):
        self.hand = []
        self.user_name = user_name

    def get_total_points_of_hand(self):
        pass

    def show_hand(self):
        pass

    def add_card_to_hand(self, list_of_cards):
        pass

    @abstractmethod
    def game_decision(self):
        pass







