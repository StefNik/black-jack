
import random


class CardUtils:

    @staticmethod
    def get_possible_suits():
        return ["S", "C", "H", "D"]

    @staticmethod
    def get_possible_colors():
        return ["R", "B"]

    @staticmethod
    def get_possible_numbers():
        possible_numbers = ["{}".format(x) for x in range(2, 11)]
        possible_numbers.extend(["J", "Q", "K", "A"])
        return possible_numbers


class Card:

    def __init__(self, suit, color, number):
        if number not in CardUtils.get_possible_numbers():
            raise RuntimeError("the number passed to the card is not valid")

        if suit not in CardUtils.get_possible_suits():
            raise RuntimeError("the suit passed to the card is not valid")

        if color not in CardUtils.get_possible_colors():
            raise RuntimeError("the number passed to the card is not valid")

        self.suit = suit
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number

    def get_suit(self):
        return self.suit

    def show(self):
        print("The card is: {}{}{}".format(self.number,self.suit,self.color))


class Deck:

    def __init__(self):
        self.deck = []

    def init_deck(self):
        for i_col in CardUtils.get_possible_colors():
            for i_suit in CardUtils.get_possible_suits():
                for i_num in CardUtils.get_possible_numbers():
                    self.deck.append(Card(i_suit, i_col, i_num))

    def get_deck(self):
        return self.deck

    def suffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for card in self.deck:
            card.show()


class Player:
    pass


if __name__ == '__main__':
    d = Deck()
    d.init_deck()
    d.print_deck()
    print()
    d.suffle_deck()
    d.print_deck()
    print()
