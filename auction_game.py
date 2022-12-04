from random import shuffle


def get_money():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10]


class Player:
    current_artifact = None

    def __init__(self, _name):
        self.name = _name
        self.money = get_money()
        self.artifacts_won = []
        self.score = 0.0
        self.bid = 0
        self.bids = []

    def add_artifact(self, artifact):
        self.artifacts_won.append(artifact)
        self.score += artifact

    def bid_in_auction(self, _bid):
        if _bid is None:
            _bid = int(input(f'What is {self.name}\'s bid on {str(Player.current_artifact)}? '))
        self.bid = _bid
        self.bids.append(_bid)
        self.money.remove(_bid)
    

    def get_total_money(self):
        total = 0
        for cash in self.money:
            total += cash
        return total
    

    def leftovers(self):
        # add leftover money to this player's score to settle ties
        total = self.get_total_money()
        self.score += total/100


def get_artifacts():
    art = [1, 2, 3, 4, 1, 2, 3, 4, 0]
    shuffle(art)
    return art # 1, 2, 3, 4, 0,   ==   J, Q, K, A, Joker


def bid_match(players, match_value):
    # key -> value concept
    for k in players:
        if k.bid == match_value:
            print(k.name)
            return k


def score_match(players, match_value):
    # key -> value concept
    for k in players:
        if k.score == match_value:
            return k


def score_helper(things):
    '''
    Returns True if there is a tie present in `things` list.
    Returns the highest number in `things` if there is not a tie in the top two things.
    '''
    things.sort()
    if things[-1] == things[-2]:
        return True
    else:
        return things[-1]


def play(players):
    p_one, p_two, p_three = players
    game_artifacts = get_artifacts()


    def bidding_round(sel_players): # sel_players -> selected players. Just wanted/needed something different
        '''
        Handles players bidding on an artifact.
        Recursively calls itself again if there is a tie in the bidding.
        Returns the auction winner (Player object) when found.
        '''
        # each player bids
        bids = []
        for p in sel_players:
            p.bid_in_auction(None)
            bids.append(p.bid)

        # determine the winner
        sh_result = score_helper(bids)
        if type(sh_result) is int:
            return bid_match(sel_players, sh_result)
        elif sh_result:
            remaining_players = []
            if p_one.bid > p_two.bid:
                remaining_players.append(p_one)
                remaining_players.append(p_three)
            elif p_two.bid > p_one.bid:
                remaining_players.append(p_two)
                remaining_players.append(p_three)
            elif p_two.bid > p_three.bid:
                remaining_players.append(p_one)
                remaining_players.append(p_two)
            else:
                remaining_players = sel_players
            # do another round of bidding with the remaining players
            bidding_round(remaining_players)


    while len(game_artifacts) != 0:
        Player.current_artifact = game_artifacts.pop() # this sets the class attribute so all Players know what they are bidding on
        # reset player bids
        for p in players:
            p.bids = []
        auction_winner = bidding_round(players)
        auction_winner.add_artifact(Player.current_artifact)
        # return bids to players that lost the auction
        losers = [p for p in players if p != auction_winner]
        for p in losers:
            for cash in p.bids:
                p.money.append(cash)
            p.money.sort()
    
    # add leftover money to each player's score
    for p in players:
        p.leftovers()

    # get the player object of the player with the highest score (doesn't account for ties currently, but are ties possible?)
    scores = []
    for p in players:
        scores.append(p.score)
    sh_result = score_helper(scores)
    if type(sh_result) is int:
        game_winner = bid_match(players, sh_result)
    elif sh_result:
        pass # this could handle ties in the future
    return game_winner


if __name__ == '__main__':
    players = [Player('X'), Player('Gamer'), Player('Evan')]
    the_winner_yippee = play(players)
    print(the_winner_yippee)