# Author:   Evan Samano
# Date:     November 13th, 2022
# Version:  1a
# Desc:     The objective of this project is to use natural seleciton to find a strategy for playing the card game "Auction."
import sys
import auction_simulation as auction

if __name__ == '__main__':
    args = sys.argv
    # args[1] should specify which simulation to load
    # args[2] should specify how many games to simulate

    if len(args) < 2:
        sim_to_load = input('Which simulation would you like to load? ')
        num_gens = int(input('How many genrations would you like to simulate? '))
    else:
        sim_to_load = args[1]
        num_gens = int(args[2])
    
    print(sim_to_load, num_gens)
    auction.simulate(num_gens)