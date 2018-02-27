import numpy as np
import scr.SamplePathClass as SamplePathSupport
import scr.FigureSupport as Fig

class Game:
    def __init__(self, id, prob_head):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)
        self._probHead = prob_head          # probability of flipping a head
        self._countWins = 0                 # number of wins,set to 0 to begin

    def simulate(self, n_of_flips):

        count_tails = 0                     # number of consecutive tails so far, set to 0 to begin

        # flip the coin 20 times
        for i in range(n_of_flips):

            # in the case of flipping a heads
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:        # if the series is..., T, T, H
                    self._countWins += 1    # increase the number of wins by 1
                count_tails = 0             # the tails counter needs to be reset to 0 because a heads was flipped

            # in the case of flipping a tails
            else:
                count_tails += 1            # increase tails count by one

    def get_reward(self):
        # calculate the reward from playing a single game
        return 100*self._countWins - 250

class SetofGames:
    def __init__(self, prob_head, n_games):
        self._gameRewards = []              # create an empty list where rewards will be stored

        # simulate the games
        for n in range(n_games):
            # create a new game
            game = Game(id=n, prob_head=prob_head)
            #simulate the game with 20 flips
            game.simulate(20)
            # store the reward
            self._gameRewards.append(game.get_reward())

    def Outcomes(self):
        return Outcomes(self)

    def get_rewards(self):
        return self._gameRewards


class Outcomes:
    def __init__(self, simulated_game):
        self._simulateGame = simulated_game

    def get_ave_reward(self):
        """ returns the average reward from all games"""
        return sum(self._simulateGame.get_rewards())/len(self._simulateGame.get_rewards())

    def get_sample_path_get_Rewards(self):
        return self._simulateGame.get_rewards()

# run trial of 1000 games to calculate expected reward
games = SetofGames(prob_head=0.5, n_games=1000)
gamesOutcomes = games.Outcomes()

# print the average reward
print('Expected reward when the probability of heads is 0.5:', gamesOutcomes.get_ave_reward())


# QUESTION 1
# plot the histogram
Fig.graph_histogram(observations=games.get_rewards(), title='Histogram of Game Rewards',
                    x_label='Rewards', y_label='Number of Games')


# QUESTION 2
# plot the sample path
SamplePathSupport.graph_sample_path(
    sample_path=games.get_rewards(),
    title='Rewards Path',
    x_label='Games',
    y_label='Rewards')