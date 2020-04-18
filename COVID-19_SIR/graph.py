# function to plot the graph
import matplotlib.pyplot as plt 

def plot(Infected, train_infected, test_infected, time_vector_1, time_vector_2, test_time):
	#  plotting infected cases
	plt.plot(time_vector_2, Infected, label = "Infected")
	#  scattering training data set points
	plt.scatter(time_vector_1, train_infected, label= "Training Data", color= "red",  marker= "*", s=30)
	#  scattering testing data set points
	plt.scatter(test_time, test_infected, label= "Test Data", color= "violet",  marker= "*", s=30)  

	plt.grid()
	plt.legend()

	plt.xlabel("Time")
	plt.ylabel("Number of Infected cases")

	plt.show()