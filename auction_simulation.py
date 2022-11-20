from auction_game import play, Player


class Agent(Player):
    def __init__(self):
        super(Agent, self).__init__()


def simulate_game(num_gens):
    current_gen = new_gen()
    for i in range(num_gens):
        current_gen = sim_gen(current_gen)


def sim_gen(agents):
    # create a generation
        # agents = list of players (300 of them for 100 1v1v1 games?)
    # have them play games against each other
        # for i in range(num of games): 
    winner = play(agents)
    # create list of fitness and track each player
    # at the end of the generation, have top 50% reproduce twice each to create the next generation
    pass


def new_gen():
    # reutrn a new generation, randomly generated if no parameters? or separate functions for random and reproduction
    pass