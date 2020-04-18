# importing required modules

# my modules
from SIR import infected, population

# Number of infected cases at t = 0 (0th Day)
I0 = infected[0]

# S -> Number of Susceptible people at t = 0
# I -> Number of Infected cases at t = 0
# beta -> infection rate
# gamma -> 1 / duration_of_infection

# To compute beta:
# Let a susceptible person come in contact with "k" infected people per day 
# and let "p" be the probability of getting infected 
# --> beta = k * p

def initial_parameters():
    
    S = population
    I = I0
    beta =  0.23
    gamma = 0.055
    
    parameters = [S, I, 0, beta, gamma]
    return parameters 