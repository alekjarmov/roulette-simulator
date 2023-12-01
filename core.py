import matplotlib.pyplot as plt  # type: ignore


def gain_at_some_point(money_history) -> bool:
    # return wether there was a point where the money was greater than the initial money
    starting_money = money_history[0]
    for money in money_history:
        if money > starting_money:
            return True
    return False


def plot_money_history(money_history, title='Money vs Number of Bets', change_colors=False):
    plt.plot(money_history)
    plt.xlabel('Number of Bets')
    plt.ylabel('Money')
    plt.title(title)

    if change_colors:
        ax = plt.gca()
        if gain_at_some_point(money_history):
            ax.set_facecolor('xkcd:light green')
        else:
            ax.set_facecolor('xkcd:light red')

    plt.show()