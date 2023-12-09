import random


class Roulette:
    MAX_NUMBER = 36
    MIN_NUMBER = 0

    def __init__(self, num_betting_fields=None):
        self.num_betting_fields = num_betting_fields

    def spin(self):
        return random.randint(self.MIN_NUMBER, self.MAX_NUMBER)

    def make_bet(self, bet_amount):
        return self.__calculate_bet(bet_amount, self.num_betting_fields)

    def make_custom_bet(self, bet_amount, num_betting_fields):
        """
        The difference between this function and `make` is that this one
        allows you to set the number of betting fields
        """
        return self.__calculate_bet(bet_amount, num_betting_fields)

    def make_even_bet(self, bet_amount):
        return self.__calculate_bet(bet_amount, self.MAX_NUMBER // 2)

    def make_single_bet(self, bet_amount):
        return self.__calculate_bet(bet_amount, 1)

    def __calculate_bet(self, bet_amount, num_betting_fields):
        """
            Function that makes a bet and returns the amount of money won or
            lost, if you lose a bet it returns a negative number
        """
        num = self.spin()
        if self.is_win(num_betting_fields, num):
            return bet_amount * self.get_bet_coefficient(num_betting_fields)
        else:
            return -bet_amount

    @staticmethod
    def get_bet_coefficient(num_betting_fields):
        return (36 / num_betting_fields) - 1

    @staticmethod
    def is_win(num_betting_fields, spin_result):
        return spin_result in range(1, num_betting_fields + 1)


# roulette = Roulette(34)
# money = 11000
# for i in range(10):
#     money += roulette.make_bet(1000)
#     print(money)
