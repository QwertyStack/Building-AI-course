############
#EXERCISE 3#
############

print('\n\nEXERCISE 3\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Let the elevation at each point on the mountain be stored in array h of size 100. The elevation at the leftmost point is thus stored 
# in h[0] and the elevation at the rightmost point is stored in h[99].

# If we plot the elevation values, they look like something like this: 

# The following program starts at a random position and keeps going to the right until Venla can no longer go up. To make it easier to 
# avoid falling off the map at the boundaries, we set both h[0] and h[100] equal to zero which is lower than any of the values in between.

# You can see the result in the above chart where the starting point is marked with a small green box and the point where Venla stops is 
# marked with a small red triangle. This works fine as long as the summit is to her right, but maybe it is to the left?

# Edit the program so that Venla doesn't stop climbing if she can go up either by moving left or right. If both ways go up, either one is 
# good. To check how your climbing algorithm works in action, you can plot the results of your hill climbing using the Plot button. The 
# summit will be marked with a blue triangle. 

import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 
w = [random.random()/3, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/6.)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]
h[0] = 0.0; h[99] = 0.0

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        if h[x + 1] > h[x]:
            x = x + 1         # right is higher, go there
            summit = False    # and keep going
    return x


def main(h):

    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

# main(h)


# ------------SOLUTION:---------------
import math
import random             	# just for generating random mountains
import matplotlib.pyplot as plt                                 	 

# generate random mountains                                                                               	 
w = [random.random()/3, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/6.)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]
h[0] = 0.0; h[99] = 0.0

plt.plot(h, 'r')
plt.show()


def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        if h[x + 1] > h[x]:
            x = x + 1         # right is higher, go there
            summit = False    # and keep going
        elif h[x-1] > h[x]:
            x = x - 1         # left is higher, go there
            summit = False    # and keep going
    return x


def main(h):

    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

print("-----intermediate solution-----")
main(h)





'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Let the elevation at each point on the mountain be stored in array h of size 100. The elevation at the leftmost point is thus stored in 
# h[0] and the elevation at the rightmost point is stored in h[99].

# Here's an example chart. The green box represents Venla's starting position, and the red triangle marks the point where Venla stops. 
# A blue triangle (not shown here) marks the summit. 

#  The following program starts at a random position and keeps going to the right until Venla can no longer go up. However, perhaps the 
# mountain is a bit rugged which means it's necessary to look a bit further ahead.

# Edit the program so that Venla doesn't stop climbing as long as she can go up by moving up to five steps either left or right. If there 
# are multiple choices within five steps that go up, any one of them is good. To check how your climbing algorithm works in action, you 
# can plot the results of your hill climbing using the Plot button. As a reminder, the summit will be marked with a blue triangle. 

import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        if h[x + 1] > h[x]:
            x = x + 1         # right is higher, go there
            summit = False    # and keep going
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

# main(h)


#----------SOLUTION------------
import math
import random
import numpy as np
import io
from io import StringIO
import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        for x_new in range(max(0, x-5), min(99, x+5)):
            if h[x_new] > h[x]:
                x = x_new        # right is higher, go there
                summit = False    # and keep going
            elif h[x_new] > h[x]:
                x = x_new         # left is higher, go there
                summit = False    # and keep going
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)

print("\n-----ADVANCED solution-----")
main(h)




#--------------------------------------------------------------------------------------------
############
#EXERCISE 4#
############
print('\n\nEXERCISE 4\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''

# Recall the program that prints out the word 'dog' with 20% probability. Modify the program so that it prints either the word 'dog' or the 
# word 'cat' (but never both, because either you're a dog person or a cat person, but not both, right?)

# Change the probability of the word 'dog' to be 80% probability (because apparently there are more dog lovers than cat lovers in the world) 
# so that the probability of the word 'cat' is 20%.

import random

def main():
    prob = 0.20
    if random.random() < prob:
        print('dog')

# main()


# ------------SOLUTION-----------
import random

def main():
    prob = 0.20
    if random.random() > prob:
        print('dog')
    else:
        print('cat')

print("-------------intermediate solution---------")
main()




'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Write a program that prints "I love" followed by one word: the additional word should be 'dogs' with 80% probability, 'cats' with 10% 
# probability, and 'bats' with 10% probability.

# Here's an example output:

# I love bats

import random

def main():

    favourite = "bats"  # change this
    print("I love " + favourite) 


# main()

# ----------SOLUTION----------
import random

def main():
    prob_dog = 0.8
    prob2 = 0.9
    rand = random.random()

    if rand < prob_dog:
        favourite = "dogs"
    elif rand < prob2:
        favourite = "cats"
    else:
        favourite = "bats"
    
    print("I love " + favourite)

print("\n-------------advanced solution---------")
main()







#--------------------------------------------------------------------------------------------
############
#EXERCISE 5#
############
print('\n\nEXERCISE 5\n')
'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''

# Suppose the current solution has score S_old = 150 and you try a small modification to create a new solution with score 
# S_new = 140. In the greedy solution, this new solution wouldn't be accepted because it would mean a decrease in the score. 
# In simulated annealing, the new solution is accepted with a certain probability as explained above.

# Modify the accept_prob function so that it returns the probability of accepting the new state using simulated annealing. The 
# program should take the two score values (the current and the new) and the temperature value as arguments.

# prob=exp(–(Sold​–Snew​)÷T)

import random

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing

    if S_new > S_old:
        return 1.0
    else:
        return 0.0

# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)



# -----------SOLUTION------------
import random
import numpy as np


def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing
    if S_new > S_old:
        return 1.0
    else:
        return np.exp(-(S_old-S_new)/T)

# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

print("-----advanced solution-----")
print(accept_prob(150, 140, 5))
accept(150, 140, 5)




#--------------------------------------------------------------------------------------------
############
#EXERCISE 6#
############
print('\n\nEXERCISE 6\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# 1D simulated annealing: modify the program below to use simulated annealing instead of plain hill climbing. In simulated 
# annealing the probability of accepting a solution that lowers the score is given by prob = exp(-(S_old - S_new)/T). Setting 
# the temperature T and gradually decreasing can be done in many ways, some of which lead to better outcomes than others. A 
# good choice in this case is for example: T = 2*max(0, ((steps-step*1.2)/steps))**3.

# Running the code produces something like the following chart, where the black box marks the starting point. The code below 
# uses the plain hill-climbing strategy to only go up towards a peak. The solution is marked by a red star. As you can see, the 
# hill-climbing strategy tends to get stuck in local optima. 

# Your task is to modify the code to use simulated annealing. Use the cooling schedule for setting the temperature provided 
# above, and modify the acceptance criterion from only accepting upward moves to accepting also downward moves with the proper 
# probability. Remember that in this exercise the score in simulated annealing is the height of a given location on the mountain.
# Also note that you will need to handle T=0 case separately, since the acceptance probability for a worse score should be zero 
# for zero temperature, but the formula used for the probability will result in division by zero. 


# HINT
# You can experiment with different cooling schedules. One example that should work okay is 
# T = max(0, ((steps - step)/steps)**3-.005) where step is the current iteration and steps is the total number of iterations. 
# You don't have to change the number of iterations from steps = 3000. 

import math, random        	# just for generating random mountains                                 	 
import numpy as np

n = 10000 # size of the problem: number of possible solutions x = 0, ..., n-1

# generate random mountains                                                                               	 
def mountains(n):
    h = [0]*n
    for i in range(50):
        c = random.randint(20, n-20)
        w = random.randint(3, int(math.sqrt(n/5)))**2
        s = random.random()
        h[max(0, c-w):min(n, c+w)] = [h[i] + s*(w-abs(c-i)) for i in range(max(0, c-w), min(n, c+w))]

    # scale the height so that the lowest point is 0.0 and the highest peak is 1.0
    low = min(h)
    high = max(h)
    h = [y - low for y in h]
    h = [y / (high-low) for y in h]
    return h

h = mountains(n)

# start at a random place
x0 = random.randint(1, n-1)
x = x0

# keep climbing for 5000 steps
steps = 5000

def main(h, x):
    n = len(h)
    # the climbing starts here
    for step in range(steps):
        # this is our temperature to be used for simulated annealing
        # it starts large and decreases with each step. you don't have to change this
        T = 2*max(0, ((steps-step*1.2)/steps))**3

        # let's try randomly moving (max. 1000 steps) left or right
        # making sure we don't fall off the edge of the world at 0 or n-1
        # the height at this point will be our candidate score, S_new
        # while the height at our current location will be S_old
        x_new = random.randint(max(0, x-1000), min(n-1, x+1000))

        if h[x_new] > h[x]:
            x = x_new           # the new position is higher, go there
        else:
            pass               # add simulated annealing here. remember to handle T=0
                               # correctly!

    return x

x = main(h, x0)
# print("ended up at %d, highest point is %d" % (x, np.argmax(h)))


# --------------------SOLUTION----------------------------
import math
import random
import numpy as np
import io
from io import StringIO
import math, random        	# just for generating random mountains                                 	 
import numpy as np

n = 10000 # size of the problem: number of possible solutions x = 0, ..., n-1

# generate random mountains                                                                               	 
def mountains(n):
    h = [0]*n
    for i in range(50):
        c = random.randint(20, n-20)
        w = random.randint(3, int(math.sqrt(n/5)))**2
        s = random.random()
        h[max(0, c-w):min(n, c+w)] = [h[i] + s*(w-abs(c-i)) for i in range(max(0, c-w), min(n, c+w))]

    # scale the height so that the lowest point is 0.0 and the highest peak is 1.0
    low = min(h)
    high = max(h)
    h = [y - low for y in h]
    h = [y / (high-low) for y in h]
    return h

h = mountains(n)

# start at a random place
x0 = random.randint(1, n-1)
x = x0

# keep climbing for 5000 steps
steps = 5000

def main(h, x):
    n = len(h)
    # the climbing starts here
    for step in range(steps):
        # this is our temperature to be used for simulated annealing
        # it starts large and decreases with each step. you don't have to change this
        T = 2*max(0, ((steps-step*1.2)/steps))**3

        # let's try randomly moving (max. 1000 steps) left or right
        # making sure we don't fall off the edge of the world at 0 or n-1
        # the height at this point will be our candidate score, S_new
        # while the height at our current location will be S_old
        x_new = random.randint(max(0, x-1000), min(n-1, x+1000))

        if h[x_new] > h[x]:
            x = x_new           # the new position is higher, go there
        else:
            if T != 0:
                if random.random() < np.exp(-(h[x]-h[x_new])/T):
                    x = x_new          

    return x

print("-----intermediate solution-----")
x = main(h, x0)
print("ended up at %d, highest point is %d" % (x, np.argmax(h)))




'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Let's use simulated annealing to solve a simple two-dimensional optimization problem. The following code runs 50 optimization 
# tracks in parallel (at the same time). It currently only looks around the current solution and only accepts moves that go up. 
# Modify the program so that it uses simulated annealing.

# Remember that the probability of accepting a solution that lowers the score is given by prob = exp(–(S_old - S_new)/T). 
# Remember to also adjust the temperature in a way that it decreases as the simulation goes on, and to handle T=0 case correctly.

# Your goal is to ensure that on the average, at least 30 of the optimization tracks find the global optimum (the highest peak).

import numpy as np
import random

N = 100     # size of the problem is N x N                                      
steps = 3000    # total number of iterations                                        
tracks = 50

# generate a landscape with multiple local optima                                          
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points                                                               
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x
    global y

    for step in range(steps):
        # add a temperature schedule here
        T = 1
        # update solutions on each search track                                     
        for i in range(tracks):
            # try a new solution near the current one                               
            x_new = np.random.randint(max(0, x[i]-2), min(N, x[i]+2+1))
            y_new = np.random.randint(max(0, y[i]-2), min(N, y[i]+2+1))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # change this to use simulated annealing
            if S_new > S_old:
                x[i], y[i] = x_new, y_new   # new solution is better, go there       
            else:
                pass                        # if the new solution is worse, do nothing

    # Number of tracks found the peak
    print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])) 
# main()


# ------------------SOLUTION----------------
import numpy as np
import random

N = 100     # size of the problem is N x N                                      
steps = 3000    # total number of iterations                                        
tracks = 50

# generate a landscape with multiple local optima                                          
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points                                                               
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x
    global y

    for step in range(steps):
        # add a temperature schedule here
        T = 2*max(0, ((steps-step*1.2)/steps))**3
        # update solutions on each search track                                     
        for i in range(tracks):
            # try a new solution near the current one                               
            x_new = np.random.randint(max(0, x[i]-2), min(N, x[i]+2+1))
            y_new = np.random.randint(max(0, y[i]-2), min(N, y[i]+2+1))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # change this to use simulated annealing
            if S_new > S_old:
                x[i], y[i] = x_new, y_new   # new solution is better, go there       
            else:
                if T != 0:
                    if random.random() < np.exp(-(S_old - S_new)/T):
                        x[i], y[i] = x_new, y_new
    # Number of tracks found the peak
    print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])) 

print("\n-----advanced solution-----")
main()
