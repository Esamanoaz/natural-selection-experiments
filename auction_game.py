from random import shuffle


def get_artifacts():
    return shuffle([1, 2, 3, 4, 1, 2, 3, 4, 0]) # 1, 2, 3, 4, 0,   ==   J, Q, K, A, Joker


def get_money():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10]


class Player:
    def __init__(self, _money=get_money()):
        self.money = _money
        self.artifacts_won = []
        self.score = 0
        self.bid = 0
    

    def add_artifact(self, artifact):
        self.artifacts_won.append(artifact)
        self.score += artifact
    

    def bid(self, _bid=input('What is this player\'s bid? ')):
        self.bid = _bid


def play(players):
    game_artifacts = get_artifacts()
    p_one, p_two, p_three = players

    while len(game_artifacts) != 0:
        current_artifact = game_artifacts.pop() # way to set variable for all class objects, even after they have been initiliazed?
        # Players bid on current artifact
        for p in players:
            p.bid()
        # Decide who won
        # create a dictionary with key "player's bid" to value "player object"
        bids = {}
        for p in players:
            bids[p.bid] = p
        # get the player object of the player with the highest bid
        auction_winner = leaderboard[[p_one.score, p_two.score, p_three.score].sort()[-1]]
        auction_winner.add_artifact(current_artifact)
        

    # create a dictionary with key "player's score" to value "player object"
    leaderboard = {}
    for p in players:
        leaderboard[p.score] = p
    # get the player object of the player with the highest score (doesn't account for ties currently, but are ties possible?)
    game_winner = leaderboard[[p_one.score, p_two.score, p_three.score].sort()[-1]]
    return game_winner