# importing required modules

# standard modules
import sys

# third party modules
from scipy.integrate import odeint
from scipy.optimize import minimize

# my modules
import infected_cases.py
from model_parameters import initial_parameters
from graph import plot

# accept country name as a terminal input
if(sys.argv[1]):
	country = sys.argv[1]
else:
	exit()

# get list of infected cases
infected = infected_cases.get_cases(country)

if(infected == "Error"):
	exit()

# population of chosen country
population = infected_cases.get_population(country)

if(population == "Error"):
	exit()

# number of days cases have been reported for 
recorded_days = len(infected)

# number of days the model should be trained for 
T_train = len(infected) - 5
# number of days the model should predict the number of cases
T_predict = 300

# time vector for training
t1 = list()
for i in range(T_train):
	t1.append(i)

# time vector for predicting
t2 = list()
for i in range(T_predict):
	t2.append(i)

# testing and training data
train_data = infected[:T_train]
test_data = infected[T_train:]

# test time vector
test_t = list() 
for i in range(len(train_data), len(infected)):
	test_t.append(i)

# calculate derivatives
def SEIR(y, t, beta, gamma):
	
	S, I, R = y

	dS = (-1 * beta * S * I)  / population
	#dE = ( (beta * S * I) / population )  - (alpha * E)
	#dI = (alpha * E) - (gamma * I)
	dI = ( (beta * S * I) / population ) - (gamma*I)
	dR = gamma * I

	return [dS, dI, dR]

# Initial model parameters :
# PARAMS[0] = S0
# PARAMS[1] = I0
# PARAMS[2] = R0 (0)
# PARAMS[3] = beta
# PARAMS[4] = gamma
PARAMS = model_parameters.initial_parameters()

def MSE(params):
	mse = 0
	Compartment = odeint(SEIR, PARAMS, t1, args = tuple(params))
	Compartment_infected = Compartment[:, 1]
	for i in range(T_train):
		mse += (Compartment_infected[i] - infected[i])**2
	return mse

# Upper and lower bound on the model parameters 
b = (0,1)
# Same bounds on both parameters
bnds = (b, b)

# Estimating model parameters by trying to fit the 
# number of infected cases with real world data

# Updating the parameters to minimize MSE
optimized_sol = minimize(MSE, PARAMS, bounds = bnds)

# Updated parameters: 
beta = optimized_sol.x[0]
gamma = optimized_sol.x[1]
PARAMS_U = tuple(optimized_sol.x)

# solve ODE
Compartment = odeint(SEIR, PARAMS[:3], t2, args = PARAMS_U)
Compartment_infected = Compartment[:, 1]

# Reproductive number
R0 = beta/gamma
print(f"R0 = {R0}")

# Plot the model's prediction
plot(Compartment_infected, infected[0:T_train], infected[T_train:], t1, t2, test_t)