from unittest import TestCase
from BlackJackPcg.Card import Card

from BlackJackPcg.Utils import CardUtils


class TestCard(TestCase):

    def test_card_for_suit(self):
        flag = False
        try:
            Card("asd", CardUtils.get_possible_colors()[0], CardUtils.get_possible_numbers()[0])
        except RuntimeError:
            flag = True

        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_for_color(self):
        flag = False
        try:
            Card(CardUtils.get_possible_suits()[0], "asd", CardUtils.get_possible_numbers()[0])
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_for_number(self):
        flag = False
        try:
            Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0], "asd")
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_creation(self):
        flag = True
        try:
            Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0], CardUtils.get_possible_numbers()[0])
        except RuntimeError:
            flag = False

        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_get_color_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0], CardUtils.get_possible_numbers()[0])

        # act
        col = c.get_color()

        # assert
        self.assertTrue(col in CardUtils.get_possible_colors())


