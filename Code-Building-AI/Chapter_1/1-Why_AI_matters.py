'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''

import numpy as np
import matplotlib.pyplot as plt

def example_plot():
    # generate a 30-by-50 array of random numbers
    x = np.random.rand(30, 50)
    # the following code that will plot the numbers as colors would normally
    # be hidden from you, so again, you won't have to worry about it.
    # try clicking the 'Plot' button to see the outcome.
    plt.figure(figsize=(3,5))
    plt.axis('off')
    plt.imshow(x, cmap='Set3')


# --------- EXERCISE 0 ---------#
# Generar salida correcta: Test Failed: AssertionError: 'Welcome Emma!' != 'Welcome to Building AI!'
# you can define your own functions
def greet(name):
    print("Welcome " + name + "!")

# go ahead and enter your own name in variable 'name' below to get a warm welcome from us.
# to pass the test, you should change the name to "to Building AI" (note the word 'to')
def main():
    name = "Emma"
    greet(name)

# main()

#---------------SOLUTION-----------------
def greet(name):
    print("Welcome " + name + "!")
def main():
    name = "to Building AI"
    greet(name)

print("-----intermediate solution-----")
main()




'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''


# --------- EXERCISE 0 ---------#
# Solving this exercise will be helpful in the first actual exercise
# (Exercise 1), so consider using this as an opportunity to warm up. 
#
# Your task is the define a function that returns the so called 
# factorial: for any non-negative integer n, the factorial is defined
# as 1 * 2 * ... * n. For example, factorial(5) = 1*2*3*4*5 = 120.
#
# Hint: the simplest way to compute the factorial is to use a
# recursive function, or in other words, a function that calls 
# itself as in 
#     factorial(n) = n * factorial(n-1)
# The recursion should terminate at factorial(0) = 1 so that we
# don't create an infinite loop.

#SOLUTION:
def factorial(n): 
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)

print("\n-----ADVANCED solution-----")
print(factorial(6))              # this should print 720