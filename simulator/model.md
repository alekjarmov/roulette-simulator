# Model explanation

Our model of the roulette is an European style roulette, that means that the black and red numbers go from 1 to 36 and there is one 0 (for example in American roulette there are two fields with 0). The way the betting works is that in our model you can't pick which numbers to vote on, but what is picked is the amount of numbers that are bet on. This is because without losing generality all the betting strategies can be shown like that. So if we are are voting a on k fields, the model uniformly picks a number in the range [0, 36] and if the number is in the range [1, k] the bet is won, otherwise the bet is lost. The formula for calculating the winning coefficient of the bet is (36 / num_betting_fields) - 1.

The code implementation of the model is the following:

```python

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
    
    def make_specific_single_bet(self, bet_amount, number):
        num = self.spin()
        return bet_amount*35 if num == number else -bet_amount
    
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

```