def get_artifacts():
    return ['J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'joker', 'joker']


def get_money():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10]


class Player:
    def __init__(self, _money):
        self.money = _money
        self.artifacts_won = []
        self.scoring = {
            'J': 1,
            'Q': 2,
            'K': 3,
            'A': 4
        }
    

    def cal_score(self):
        score = 0
        for a in self.artifacts_won:
            score += self.scoring[a]
        return score


def play(players):
    game_artifacts = get_artifacts()
    p_one, p_two, p_three = players

    while len(game_artifacts) != 0:
        pass

    # create a dictionary with key "player's score" to value "player object"
    leaderboard = {}
    for p in players:
        leaderboard[p.cal_score()] = p
    # get the player object of the player with the highest score
    winner = leaderboard[[p_one.cal_score(), p_two.cal_score(), p_three.cal_score()].sort()[-1]]
    return winner