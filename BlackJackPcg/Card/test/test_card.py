from unittest import TestCase
from BlackJackPcg.Card import Card

from BlackJackPcg.Utils import CardUtils

import random

import contextlib
import io


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

    def test_get_suit_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0],
                 CardUtils.get_possible_numbers()[0])

        # act
        suit = c.get_suit()

        # assert
        self.assertTrue(suit in CardUtils.get_possible_suits())

    def test_get_number_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0],
                 CardUtils.get_possible_numbers()[0])

        # act
        number = c.get_number()

        # assert
        self.assertTrue(number in CardUtils.get_possible_numbers())

    def test_show_func_list_input(self):
        # arrange
        c = Card(
            random.choice(CardUtils.get_possible_suits()),
            random.choice(CardUtils.get_possible_colors()),
            random.choice(CardUtils.get_possible_numbers())
        )

        with io.StringIO() as buf:
            # act
            with contextlib.redirect_stdout(buf):
                c.show()
            # assert
            self.assertTrue(buf.getvalue().strip() == c.to_string())
