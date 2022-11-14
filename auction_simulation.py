def simulate(num_gens):
    current_gen = new_gen()
    for i in range(num_gens):
        current_gen = sim_gen(current_gen)


def sim_gen():
    # create a generation
    # have them play games against each other
    # create list of fitness and track each player
    # at the end of the generation, have top 50% reproduce twice each to create the next generation
    pass


def new_gen():
    # reutrn a new generation, randomly generated if no parameters? or separate functions for random and reproduction
    pass