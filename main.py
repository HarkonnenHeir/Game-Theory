import random
from random import randint

class Strategy:
    def __init__(self, name, history, score=0):
        self.name = name
        self.history = history
        self.score = score

    def choose_option(self):
        pass


class GoodGuy(Strategy):
    def choose_option(self):
        return True


class BadGuy(Strategy):
    def choose_option(self):
        return False


class Lunatic(Strategy):
    def choose_option(self):
        if (randint(1, 2)) == 1:
            return True
        else:
            return False


class Resentful(Strategy):
    def choose_option(self):
        global round
        if self.history == []:
            return True
        else:
            return self.history[round - 1]


good_guy = GoodGuy("Good Guy", [])
bad_guy = BadGuy("Bad Guy", [])
lunatic = Lunatic("Lunatic", [])
resentful = Resentful("Resentful", [])

strategies_list = [good_guy, bad_guy, lunatic, resentful]
round = 0

def compete(first_strategy, second_strategy):
    first_choice = first_strategy.choose_option()
    second_choice = second_strategy.choose_option()
    print(f"Round {round} : {first_strategy.name} chooses {first_choice} and {second_strategy.name} chooses {second_choice}.")
    first_strategy.history.append(second_choice)
    second_strategy.history.append(first_choice)

    if first_choice is True and second_choice is True:
        first_strategy.score += 5
        second_strategy.score += 5
    if first_choice is True and second_choice is False:
        second_strategy.score += 9
    if first_choice is False and second_choice is True:
        first_strategy.score += 10


for fs in strategies_list:
    for ss in strategies_list:
        fs.history = []
        ss.history = []
        round = 0
        for x in range(100):
            compete(fs, ss)
            round += 1

for strategy in strategies_list:
    print(f"{strategy.name} : {strategy.score}")

