############
#EXERCISE 7#
############

print('\n\nEXERCISE 7\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Write a program that counts the number of occurrences of "11" in an input sequence of zeros and ones. The input of the 
# program is just the sequence and it should return a single number, which is the number of occurrences of "11". 
def count11(seq):
   # define this function and return the number of occurrences as a number
   return -1

# print(count11([0, 0, 1, 1, 1, 0])) # this should print 2


# -------------------SOLUTION-------------------
def count11(seq):
    counter = 0
    i = 0
    while i < len(seq)-1:
        if seq[i] == 1 and seq[i+1] == 1:
            counter = counter + 1
        i+=1
    return counter

print("-----intermediate solution-----")
print(count11([0, 0, 1, 1, 1, 0]))






'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Write a program that generates 10000 random zeros and ones where the probability of one is p1 and the probability 
# of zero is 1-p1 (hint: np.random.choice([0,1], p=[1-p1, p1], size=10000)), counts the number of occurrences of 
# 5 consecutive ones ("11111") in the sequence, and outputs this number as a return value. Check that for p1 = 2/3, 
# the count is close to 10000 x (2/3)^5 ≈ 1316.9. 

import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.empty(10000)
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    return -1 

def main(p1):
    seq = generate(p1)
    return count(seq)

# print(main(2/3))



# ---------------------SOLUTION-----------------
import numpy as np

def generate(p1):
    return np.random.choice([0,1], p=[1-p1, p1], size=10000)

def count(seq):
    counter = 0
    i = 0
    while i < len(seq)-4:
        if seq[i] == 1 and seq[i+1] == 1 and seq[i+2] and seq[i+3] and seq[i+4]:
            counter = counter + 1
        i+=1
    return counter 

def main(p1):
    seq = generate(p1)
    return count(seq)

print("\n-----advanced solution-----")
print(main(2/3))










#---------------------------------------------------------------------------------------------------
############
#EXERCISE 8#
############

print('\n\nEXERCISE 8\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Write a program that uses statistics about the population and fishing industry employment to print out conditional 
# probabilities of each nationality given that the winner works in the fishing industry.

# The data is given in lists containing the population and the number of fishers in each country.

# Output Example
# Denmark 14.32%

# ...

# Sweden 08.45%

# Tip: Your values might be different, but the formatting should be identical. 
def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    # write your solution here

    for country, population in zip(countries, populations):
        print("%s %.2f%%" % (country, population)) # modify this to print correct results

# main()


# -------SOLUTION--------
def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    # write your solution here

    for country, fisher in zip(countries, fishers):
        print("%s %.2f%%" % (country, (fisher/total_fishers)*100)) 

print('------intermediate solution------')
main()





'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Suppose we also happen to know the gender of the lottery winner. Here are same OECD statistics as above broken 
# down by gender:

# Country 	Population 	Male fishers 	Female fishers 	Fishers (total)
# Denmark 	5,615,000 	1822 	        69 	            1891
# Finland 	5,439,000 	2575 	        77 	            2652
# Iceland 	324,000 	3400 	        400 	        3800
# Norway 	5,080,000 	11,291 	        320 	        11,611
# Sweden 	9,609,000 	1731 	        26 	            1757
# TOTAL 	26,067,000 	20,819 	        892 	        21,711

# Write a function that uses the above numbers and tries to guess the nationality of the winner when we know that 
# the winner is a fisher and their gender (either female or male).

# The argument of the function should be the gender of the winner ('female' or 'male'). The return value of the 
# function should be a pair (country, probability) where country is the most likely nationality of the winner and 
# probability is the probability of the country being the nationality of the winner.

# Output Example
# if the winner is male, my guess is he's from Finland; probability 08.56%
# if the winner is female, my guess is she's from Norway; probability 23.98%

# Tip: Your values might be different, but the formatting should be identical.

countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    # write your solution here

    guess = None
    biggest = 0.0
    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

# main()



# ----------SOLUTION-----------
countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    elif winner_gender == 'male':        
        fishers = male_fishers
    else:
        pass

    guess = None
    biggest = 0.0
    total_fishers = sum(fishers)
    total_population = sum(populations)

    for i in range(len(countries)):
        prob = (fishers[i]/total_fishers) * 100
        if biggest < prob:
            guess = countries[i]
            biggest = prob

    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))


print('\n-----ADVANCED solution------')
main()