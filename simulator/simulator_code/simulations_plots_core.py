from core import *
import statistics
import matplotlib.pyplot as plt  # type: ignore
from matplotlib.ticker import FuncFormatter
import math

def plot_money_histories(money_histories: dict, goal_money: int, limit_plots : int = 10) -> None:
    for money_history in money_histories[goal_money][:limit_plots]:
        plot_money_history(money_history, minimum_line=True)

def plot_minimum_money(money_histories: dict, goal_money: int, log_values: bool = False) -> None:
    minimum_money = []
    for money_history in money_histories[goal_money]:
        res = min(money_history)
        if log_values:
            res = math.log2(abs(res)+1)
            
        minimum_money.append(res)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(minimum_money)

    def format_ticks(value, _):
        return f'{value:.0f}'  # Adjust the formatting as needed
    
    mean = sum(minimum_money) / len(minimum_money)
    ax.axhline(mean, color='r', linestyle='dashed', linewidth=2)
    ax.text(0.05, 0.97, f'Mean: {mean:.2f}', transform=ax.transAxes, color='r')

    median = statistics.median(minimum_money)
    ax.axhline(median, color='g', linestyle='dashed', linewidth=2)
    ax.text(0.05, 0.90, f'Median: {median:.2f}', transform=ax.transAxes, color='g')

    ax.yaxis.set_major_formatter(FuncFormatter(format_ticks))
        
    plt.show()
    
def plot_successful_bets(money_histories: list, goal: int, title: str='Successful bets') -> None:
    num_bets = ['Successful' if money_history[-1] >= goal else 'Unsuccessful' for money_history in money_histories]
    plt.hist(num_bets)
    plt.title(title)
    plt.show()