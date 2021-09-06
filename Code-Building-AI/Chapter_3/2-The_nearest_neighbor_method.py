import math
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


############
#EXERCISE 15#
############

print('\n\nEXERCISE 15\n')
'''**************************************************************'''
'''************************ BEGINNER ****************************'''
'''**************************************************************'''
# What is the correct Euclidean distance between these two vectors? a = [14, 3, 0.8], b = [2, 6, 0.8]
print('-----begginer solution---')
def euclidean(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

a = [14, 3, 0.8]
b = [2, 6, 0.8]

print(euclidean(a, b))





'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Which of these calculate the Euclidean distance between two vectors correctly? You can assume that the arrays 
# a and b containing the vectors are of equal length.
def dist_A(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def dist_B(a, b):
    sum_a = 0
    sum_b = 0
    for ai in a:
        sum_a = sum_a + ai
    for bi in b:
        sum_b = sum_b + bi
    return np.sqrt((sum_a - sum_b)**2)


# ----solution-----
print("\n---intermediate solution---")
sol_A = dist_A(a,b)
sol_B = dist_B(a,b)

if sol_A == euclidean(a, b):
    print("A is the correct solution")
elif sol_B == euclidean(a, b):
    print("B is the correct solution")







'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# You are given an array x_train with multiple input vectors (the "training data") and another array x_test with one 
# more input vector (the "test data"). Find the vector in x_train that is most similar to the vector in x_test. In 
# other words, find the nearest neighbor of the test data point x_test.

# The code template gives the function dist to calculate the distance between any two vectors. What you need to add 
# is the implementation of the function nearest that takes the arrays x_train and x_test and prints the index (as 
# an integer between 0, ..., len(x_train)-1) of the nearest neighbor.

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.Inf
    # add a loop here that goes through all the vectors in x_train and finds the one that
    # is nearest to x_test. return the index (between 0, ..., len(x_train)-1) of the nearest
    # neighbor
    print(nearest)

# nearest(x_train, x_test)



# ----SOLUTION----
print("\n---advanced solution---")
x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.Inf

    for i in range(len(x_train)):
        d = dist(x_train[i], x_test)
        if d < min_distance:
            min_distance = d           
            nearest = i             # nearest vector to x_text

    print(nearest)

nearest(x_train, x_test)












# -------------------------------------------------------------------------------------------------------------
#############
#EXERCISE 16#
#############

print('\n\nEXERCISE 16\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# The program below uses the library sklearn to generate a random dataset. You don't need to be familiar with sklearn, 
# we explain all the necessary information below. Each sample in the dataset has two input features X and one binary 
# output class y. We can think of a sample as a cabin, with its size and price as its input features, and whether we 
# like it (1) or not (0) as its output class.

# The program's goal is to classify the cabins based on their nearest neighbor's class. That is, predict whether we would 
# like a cabin based on our opinion of another cabin with the most similar input features.

# The program first generates the random dataset and splits it into training and test sets. Then, for each cabin in the 
# test set, it identifies its nearest neighbor from the cabins in the train set using the distance function. However, the 
# program has very high standards and dislikes all the cabins y_predict[i] = 0.

# Your goal is to make the program smarter by predicting the output class (y_predict) for each cabin in the test set based 
# on the output class (y_train) of its nearest neighbor.
import numpy as np


# create random data with two classes
X, y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []


# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines
    
    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]

        # find the index of the nearest neighbor
        nearest = np.argmin(distances)

        # create a line connecting the points for the chart
        lines.append(np.stack((test_item, X_train[nearest])))

        # add your code here:
        y_predict[i] = 0          # this just classifies everything as 0 

    print(y_predict)


# main(X_train, X_test, y_train, y_test)



# ----SOLUTION----

print("---intermediate solution---")

# create random data with two classes
X, y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []


# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines
    
    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]

        # find the index of the nearest neighbor
        nearest = np.argmin(distances)

        # create a line connecting the points for the chart
        lines.append(np.stack((test_item, X_train[nearest])))

        # add your code here:
        y_predict[i] = y_train[nearest]

    print(y_predict)


main(X_train, X_test, y_train, y_test)







'''**************************************************************'''
'''************************ ADVANCED *****************************'''
'''**************************************************************'''
print("\n---ADVANCED solution---")


# In the basic nearest neighbor classifier, the only thing that matters is the class label of the nearest neighbor. But the 
# nearest neighbor may sometimes be noisy or otherwise misleading. Therefore, it may be better to also consider the other 
# nearby data points in addition to the nearest neighbor.

# This idea leads us to the so called k-nearest neighbor method, where we consider all the k nearest neighbors. If k=3, for 
# example, we'd take the three nearest points and choose the class label based on the majority class among them.

# The program below uses the library sklearn to generate a random dataset. You don't need to be familiar with sklearn, we 
# explain all the necessary information below. Each sample in the dataset has two input features (X) and one binary output 
# class (y). We can think of a sample as a cabin, with its size and price as its input features, and whether we like it (1) 
# or not (0) as its output class.

# The program first generates the random dataset and splits it into training and test sets. Then, for each cabin in the test 
# set, it identifies its nearest neighbor (k=1) from the cabins in the train set using the distance function. However, the 
# program has very high standards and dislikes all the cabins y_predict[i] = 0.

# Your goal is to make the program smarter by predicting the output class (y_predict) for each cabin in the test set based 
# on the majority output class (y_train) of its three nearest neighbor (k=3).

# HINTS
# Hint 1: After calculating all the distances in D (see the code below) you can use np.argsort to sort the points in 
# increasing distance.

# Hint 2: You can assume that there are only two possible class labels, 0 and 1. As this is the case, you can get the 
# majority where class by np.round(np.mean(y)) where y is the list containing the class labels of the nearest neighbors. This works by calculating the mean of the class labels and rounding it to zero in case it is less than 0.5 and one otherwise, which is the same as the majority rule.




# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []

# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    k = 3    # classify our test items based on the classes of 3 nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]

        # add your code here
        nearest = np.argmin(distances)       # this just finds the nearest neighbour (so k=1)

        # create a line connecting the points for the chart
        # you may change this to do the same for all the k nearest neigbhors if you like
        # but it will not be checked in the tests
        lines.append(np.stack((test_item, X_train[nearest])))

        y_predict[i] = 0          # this just classifies everything as 0
    
    print(y_predict)

# main(X_train, X_test, y_train, y_test)




#  ---- SOLUTION----
# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []

# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    k = 3    # classify our test items based on the classes of 3 nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]

        # add your code here
        nearest =  np.argsort(distances)      

        # create a line connecting the points for the chart
        # you may change this to do the same for all the k nearest neigbhors if you like
        # but it will not be checked in the tests
        for j in range(len(nearest)):
            if j < k:
                lines.append(np.stack((test_item, X_train[nearest[j]])))

        s = 0
        for j in range(len(nearest)):
            if j < k:
                
                s = s + y_train[nearest[j]]
        if s > 1:
            y_predict[i] = 1
        else:
            y_predict[i] = 0

    print(y_predict)

main(X_train, X_test, y_train, y_test)
