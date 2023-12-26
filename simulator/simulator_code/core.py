# Core functions

import matplotlib.pyplot as plt  # type: ignore
import math

import numpy as np

def gain_at_some_point(money_history) -> bool:
    # return wether there was a point where the money was greater than the initial money
    starting_money = money_history[0]
    for money in money_history:
        if money > starting_money:
            return True
    return False


def plot_money_history(money_history, std_dev = None, title='Money vs Number of Bets', change_colors=False, minimum_line=False, maximum_line = False, log_values = False):
    
    if log_values:
        money_history = [-math.log2(abs(v)+1) if v<0 else math.log2(v+1) for v in money_history]
        std_dev = [math.log2(v+1) for v in std_dev]
    
    plt.plot(money_history)

    if std_dev is not None:
        plt.fill_between(range(len(money_history)), np.array(money_history) - np.array(std_dev), 
                         np.array(money_history) + np.array(std_dev), color='gray', alpha=0.3, label='Standard Deviation')

    plt.xlabel('Number of Bets')
    plt.ylabel('Money')
    plt.title(title)

    if change_colors:
        ax = plt.gca()
        if gain_at_some_point(money_history):
            ax.set_facecolor('xkcd:light green')
        else:
            ax.set_facecolor('xkcd:light red')
    if minimum_line:
        plt.axhline(y=min(money_history), color='r', linestyle='-')
        plt.text(0, min(money_history), 'Minimum: ' + str(min(money_history)))
    if maximum_line:
        plt.axhline(y=max(money_history), color='g', linestyle='-')
        plt.text(0, max(money_history), 'Maximum: ' + str(max(money_history)) + ' for bet: ' + str(money_history.index(max(money_history))))
    
    plt.show()


def plot_number_of_bets(money_histories, title='Number of bets until losing all the money'):
    num_bets = [math.log10(len(money_history)) for money_history in money_histories]
    plt.hist(num_bets, bins = 100)
    plt.xlabel('log10')
    plt.ylabel('Number of bets')
    plt.title(title)
    plt.show()
