import math
import numpy as np

#############
#EXERCISE 19#
#############

print('\n\nEXERCISE 19\n')
'''**********************************************************'''
'''************************ ADVANCED ************************'''
'''**********************************************************'''
# You are given a set of three input values and you also have multiple alternative sets of three coefficients. Calculate 
# the predicted output value using the linear formula combined with the logistic activation function.

# Do this with all the alternative sets of coefficients. Which of the coefficient sets yields the highest sigmoid output?

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z):
    # add your implementation of the sigmoid function here
    print(0)

# calculate the output of the sigmoid for x with all three coefficients


# --- SOLUTION ----
print("---advanced solution---")

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z):
	print(1 / (1 + math.exp(-z)))

# calculate the output of the sigmoid for x with all three coefficients
sigmoid(((-0.5) *4) + 0.1 * 3 + 0.08 * 0)
sigmoid(((-0.2) *4) + 0.2 * 3 + 0.31 * 0)
sigmoid((0.5) *4 + ((-0.1) * 3) + 2.53 * 0)