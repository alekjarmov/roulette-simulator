from statistics import mean, stdev
from roulette import Roulette
from collections import defaultdict

def goal_money_betting_even_bet(roulette, goal_money_won, start_bet_amount,
                                transformation_loss, transformation_win, money_limit = None):
    money = 0
    bet_amount = start_bet_amount
    money_history = [money]
    bet_history = []
    while money < goal_money_won:
        if money_limit is not None and money < money_limit:
            return money_history
        prev_money = money 
        money += roulette.make_even_bet(bet_amount)
        money_history.append(money)
        bet_history.append(bet_amount)
        if money < prev_money:
            bet_amount, bet_history = transformation_loss(bet_history)
        else:
            bet_amount, bet_history = transformation_win(bet_history)
    return money_history
    

def simulate_different_goal_money(betting_type, goal_money_list, number_histories, money_limit = None, start_bet = 1):
    money_histories = defaultdict(lambda: [])

    for goal in goal_money_list:
        for _ in range(number_histories):
            money_histories[goal].append(betting_type(goal,  start_bet, money_limit))
    return money_histories

def get_successful_histories(money_histories, goals):
    successful_histories = dict()
    for goal in goals:
        successful_histories[goal] = [money_history for money_history in money_histories[goal] if money_history[-1] >= goal]

    return successful_histories


def get_mean_and_std_of_histories(money_histories, goal):
    max_length = max(len(sublist) for sublist in money_histories[goal])
    result_list = [sublist + [sublist[-1]] * (max_length - len(sublist)) for sublist in money_histories[goal]]

    mean_list = []
    std_list = []
    for i in range(max_length):
        mean_list.append(mean([l[i] for l in result_list]))
        std_list.append(stdev([l[i] for l in result_list]))
    return mean_list, std_list

def get_mean_money_won(money_histories, goal):
    histories = money_histories[goal]

    check = [h[-1] for h in histories if h[-1]>=goal]
    if len(check) == 0:
        return 0
    return mean(check)

def get_mean_money_lost(money_histories, goal):
    histories = money_histories[goal]

    check = [h[-1] for h in histories if h[-1]<goal]
    if len(check) == 0:
        return 0
    return mean(check)