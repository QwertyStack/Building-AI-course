############
#EXERCISE 1#
############

print('\n\nEXERCISE 1\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Imagine that you've been assigned the task to plan the route of a container ship loaded with pineapples. The ship starts in Panama,
# loaded with delicious Fairtrade pineapples. There are four other ports, New York, Casablanca, Amsterdam, and Helsinki, where
# pineapple-craving citizens are eagerly waiting. The ship must visit each of the four destination ports exactly once, but the order in
# which each port is visited is free. The goal is to minimize the carbon emissions, which means that a shorter route is better than a
# longer one.

# In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports exactly once.

# Have a look at the program further down the page. Go ahead and run it. You'll see that the first thing it prints is PAN AMS AMS AMS AMS.
# Nice for the sailors but bad for pineapple lovers anywhere else but Amsterdam.

# Each port is denoted by a number instead of a string: PAN is 0, AMS is 1 and so on. It is often easier to work with integer numbers
# instead of strings when programming. Keep this mapping in mind when we interpret the results of the program.

# Fix the program by adding an if statement that checks that the route includes all of the ports. In other words, check that each of the
#  numbers 0, 1, 2, 3, 4 are included in the list route.

# Do not change the print statement given in the template (although you can add more print statements for debugging purposes).

# Output Example
# PAN AMS CAS NYC HEL

# ...

# PAN CAS AMS NYC HEL

# Tip: Your values might be different, but the formatting should be identical.


def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Modify this if statement to check if the route is valid
                    if(True):
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

# main()


# ------------SOLUTION:---------------
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Modify this if statement to check if the route is valid
                    # if(0 in route and 1 in route and 2 in route and 3 in route and 4 in route):
                    if set(route) == set(range(5)):
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

                        # otra opcion
                        # print()
                        # for i in route:
                        #     print(' '+ portnames[i], end='')
print("-----intermediate solution-----")
main()


'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports
# exactly once.

# The template code below contains an incomplete permutations function which takes as input a specified route and a
# list of port names absent from that route. Modify the function so that it prints out all the possible orderings of the ports that always begin with Panama (PAN).

# The mathematical term for such orderings is a permutation. Note that your program should work for an input
# portnames list of any length. The order in which the permutations are printed doesn't matter.

# As the output the function should print each permutation on its own row, as one string, with the port names
# separated by spaces. For this, you can use the join function as follows: print(' '.join([portnames[i] for i in
# route])).

# Output Example
# PAN AMS CAS NYC HEL

# ...

# PAN CAS AMS NYC HEL

# Tip: Your values might be different, but the formatting should be identical.

# HINT:
# The easiest way to do this is by the programming technique called recursion. If you are not familiar with it,
# this is a nice opportunity to learn (see for example here). The trick is to start the recursion with the empty
# list, which we can call route. The recursive function should involve a for loop that goes through the available
# ports and for each port:
#    1. appends it to the list route
#    2. removes it from the list of available ports, and
#    3. calls the same function with the remaining ports

# When the function is called with an empty list of ports, the recursion should stop and print out the list route.

# It'll be easiest to work with integer indexes instead of the port names.

# So for example, if we start the recursion with route = [0] and ports = [1, 2, 3, 4], meaning that the first stop
# is always Panama, the first thing to do is to try each of the ports after the 1 in the route to get, for example,
# route = [0, 3] and continue the recursion with the remaining ports, for example, [1, 2, 4]. To remove item i from
# the list, you can write ports[:i]+ports[i+1:].


portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
    # Write your recursive code here

    # Print the port names in route when the recursion terminates
    print(' '.join([portnames[i] for i in route]))

# This will start the recursion with 0 ("PAN") as the first stop
# permutations([0], list(range(1, len(portnames))))


# ------------SOLUTION:---------------
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
    if len(ports) < 1:
        # Print the port names in route when the recursion terminates
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])

    # Print the port names in route when the recursion terminates

print("\n-----advanced solution-----")
# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))



# ---------------------------------------------------------------------------------------------
############
#EXERCISE 2#
############
print('\n\nEXERCISE 2\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Let's assume that the boat is relatively modern and produces 0.020 kg of CO2 emissions per kilometer for the amount of
# pineapples that we are shipping.

# The program below prints the total emissions on the route PAN, AMS, CAS, NY, HEL (in port indices route 0, 1, 2, 3, 4)
# in kilograms, which is 504.5 kg. Modify the program so that it prints out the carbon emissions of all the possible
# routes. The solution for the previous exercise should be useful here.

# Output Example
# PAN AMS CAS NYC HEL 427.1 kg

# ...

# PAN CAS AMS NYC HEL 495.5 kg

# Tip: Your values might be different, but the formatting should be identical

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # https://sea-distances.org/
    # nautical miles converted to km
    D = [
        [0, 8943, 8019, 3652, 10545],
        [8943, 0, 2619, 6317, 2078],
        [8019, 2619, 0, 5836, 4939],
        [3652, 6317, 5836, 0, 7825],
        [10545, 2078, 4939, 7825, 0]
    ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)
    co2 = 0.020

    route = [0, 1, 2, 3, 4]
    distance = D[route[0]][route[1]] + D[route[1]][route[2]] + \
        D[route[2]][route[3]] + D[route[3]][route[4]]
    emissions = distance * co2
    print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)

# main()


# ------------SOLUTION:---------------
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # https://sea-distances.org/
    # nautical miles converted to km
    # matrix distance
    D = [
        [0, 8943, 8019, 3652, 10545],
        [8943, 0, 2619, 6317, 2078],
        [8019, 2619, 0, 5836, 4939],
        [3652, 6317, 5836, 0, 7825],
        [10545, 2078, 4939, 7825, 0]
    ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)
    co2 = 0.020

    route = [0, 1, 2, 3, 4]
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    if set(route) == set(range(5)):
                        distance = D[route[0]][route[1]] + D[route[1]][route[2]
                                                                       ] + D[route[2]][route[3]] + D[route[3]][route[4]]
                        emissions = distance * co2
                        print(' '.join([portnames[i]
                                        for i in route]) + " %.1f kg" % emissions)


print("-----intermediate solution-----")
main()



'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Building on the previous solution, modify the code so that it finds the route with
# minimum carbon emissions and prints it out. Again, the program should work for any
# number of ports. You can assume that the distances between the ports are given in
# an array of the appropriate size so that the distance between ports i and j is
# found in D[i][j].

# Output Example
# PAN AMS CAS NYC HEL 240.1 kg

# Tip: Your values might be different, but the formatting should be identical.

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km
D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0]
]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)
co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions
    pass

def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing
    # this will start the recursion
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

# main()


# ------------SOLUTION:---------------
import math
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0]
]
co2 = 0.020

# these variables are initialised to nonsensical values
# the program should determine the correct values for them
smallest = math.inf
bestroute = None

def permutations_emissions(route, ports):
    global smallest, bestroute

    if len(ports) < 1:
        # emissions = co2 * sum(D[i][j] for i, j in zip(route[:-1], route[1:]))
        for i in route[:-1]:
            distance = 0
            for j in route[1:]:
                distance = D[route[route.index(j)-1]][j] + distance
            emissions = distance * co2
            if smallest > emissions:
                smallest = emissions
                bestroute = route
    else:
        for i in range(len(ports)):
            permutations_emissions(route+[ports[i]], ports[:i]+ports[i+1:])


def main():
    # this will start the recursion
    permutations_emissions([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)


print("\n-----advanced solution-----")
main()















