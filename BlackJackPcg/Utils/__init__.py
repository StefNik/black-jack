

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

    @staticmethod
    def get_card_value(card, is_ace_eleven=True):
        if card not in CardUtils.get_possible_numbers():
            raise RuntimeError("The card number passed is not a valid number.")
        if isinstance(card, int):
            return card
        if isinstance(card, str):
            if card is "A":
                if is_ace_eleven:
                    return 11
                else:
                    return 1
            else:
                return 10

