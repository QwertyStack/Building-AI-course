import numpy as np
from io import StringIO

############
#EXERCISE 11#
############

print('\n\nEXERCISE 11\n')
'''**************************************************************'''
'''************************ BEGINNER ****************************'''
'''**************************************************************'''
# What would the predicted price of a cabin be with the following details? Size: 85 m2, size of the sauna: 10m2, 
# distance to a lake: 15m, number of indoor toilets: 1, distance to next door neighbor: 100m

# input values for one mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbours

# -----SOLUTION-----

x = [85, 10, 15, 1, 100]               # input values
c = [3000, 200 , -50, 5000, 100]       # coefficient values

def predictedPrice(x, c):
    prediction = c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4]
    print(prediction)

print("-----beginner solution 1----")
predictedPrice(x, c)


# What would the predicted price of a cabin be with the following details? Size: 155m2, size of the sauna: 15m2, 
# distance to a lake: 5m, number of indoor toilets: 1, distance to next door neighbor: 200m.

# -----SOLUTION-----
x1 = [155, 15, 5, 1, 200]               # input values
c1 = [3000, 200 , -50, 5000, 100]       # coefficient values

print("-----beginner solution 2----")
predictedPrice(x1, c1)





'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Edit the code so that it prints out the prices of multiple cabins in one go. 
# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):
    # write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same

    price = 0            
    print(price)

# predict(X, c)



# ------SOLUTION------

# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):
    # write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same

    for i in range(len(X)):
        price = c[0]*X[i][0] + c[1]*X[i][1] + c[2]*X[i][2] + c[3]*X[i][3] + c[4]*X[i][4]
        print(price)

print("\n---- intermediate solution-----")
predict(X, c)







'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Edit the following program so that it can process multiple cabins that may be described by any number of details 
# (like five below), at the same time. You can assume that each of the lists contained in the list x and the 
# coefficients c contain the same number of elements. 
# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    price = 0            
    print(price)

# predict(X, c)

# ----SOLUTION-----


# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    for i in X:
        feature = np.array(i)
        coef = np.array(c)
        print( feature @ coef)

print("\n---- advanced solution-----")
predict(X, c)











# -----------------------------------------------------------------------------------------------------------------------
############
#EXERCISE 12#
############

print('\n\nEXERCISE 12\n')
'''**************************************************************'''
'''************************ BEGINNER ****************************'''
'''**************************************************************'''
# Suppose we have a data set of three points in the format of (x, y): (0, 5), (2, 9.6), and (3.2, 13.6). Your colleagues 
# have built three different models to fit the data, all of the form y = a + b*x. They have given you the coefficients of 
# their models, and they are as follows:
    # a) a=0.5, b=3.2
    # b) a=0, b=1.9
    # c) a=7.6, b=1.9

# Which of the coefficients gives the smallest squared error?

points = [[0,5], [2,9.6], [3.2,13.6]]
coef = [[0.5,3.2], [0,1.9], [7.6,1.9]]

def least_squares(points, coefficients):
    Y = []
    observed = []
    sol = []
    
    for i in range(len(coefficients)):      
        Y.append(points[i][1])                  # coeff and points have the same lenght
        for j in range(len(points)):
            c = coefficients[i][0] + coefficients[i][1]*points[j][0]    
            observed.append(c)
    
    Y = np.array(Y)
    observed = np.array(observed)
    observed = observed.reshape(3,3)
    diff = (Y - observed)**2

    diff = np.sum(diff, axis=1)
    return np.where(diff == diff.min())

 
print("----beginner solution-----")
out=least_squares(points, coef)
if out[0] == 0:
    print("the coefficient with the smallest squared error is: A) a=0.5, b=3.2")
elif out[0] == 1:
    print("the coefficient with the smallest squared error is: B) a=0, b=1.9")
elif out[0] == 2:
    print("the coefficient with the smallest squared error is: C) a=7.6, b=1.9")
else:
    print("error")





'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Modify the program so it implements the calculation of the squared error. In other words, you should 
# calculate the predicted prices for all the cabins in the data, subtract the predicted price from the actual 
# price (which is given in the data), square the difference, and add them all up.

# The program needs to work for any number of cabins and cabin features.

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        # add your code here: calculate the predicted price,
        # subtract it from the actual price yi, 
        # square the difference using (yi - prediction)**2, 
        # and add up all the differences in variable sse
        pass

    print(sse)

# squared_error(X, y, c)



# ----SOLUTION----
print("\n----intermediate solution-----")


X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        sse = sse + (yi - (xi @ c))**2

    print(sse)

squared_error(X, y, c)





'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Write a program that calculates the squared error for multiple sets of coefficient values and prints out 
# the index of the set that yields the smallest squared error: this is a poor man's version of the least 
# squares method where we only consider a fixed set of alternative coefficient vectors instead of finding 
# the global optimum. 

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for coeff in c:
        pass     # edit here: calculate the sum of squared error with coefficient set coeff and
                 # keep track of the one yielding the smallest squared error
    print("the best set is set %d" % best_index)


# find_best(X, y, c)



#  -----SOLUTION-------
print("\n----ADVANCED solution-----")

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])    

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    i = 0
    for coeff in c:        
        # edit here: calculate the sum of squared error with coefficient set coeff and
        # keep track of the one yielding the smallest squared error
        sse =  0.0
        for xi, yi in zip(X, y):
            sse = sse + (yi - (xi @ coeff))**2
        if sse < smallest_error:
            smallest_error = sse
            best_index = i
        i = i+1
    print("the best set is set %d" % best_index)

find_best(X, y, c)
















# -----------------------------------------------------------------------------------------------------------------------
############
#EXERCISE 13#
############

print('\n\nEXERCISE 13\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Try modifying the code below by adding the numbers for a sixth cabin into the data so that you have the 
# following data set. Do not change the print statements.
# cabin 1 	25 	    2 	50 	1 	500 	127,900
# cabin 2 	39 	    3 	10 	1 	1000 	222,100
# cabin 3 	13 	    2 	13 	1 	1000 	143,750
# cabin 4 	82 	    5 	20 	2 	120 	268,000
# cabin 5 	130 	6 	10 	2 	600 	460,700
# cabin 6 	115 	6 	10 	1 	550 	407,000



def main():
    np.set_printoptions(precision=1)

    x = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600]
        ]
    )   

    y = np.array([127900, 222100, 143750, 268000, 460700])

    c = np.linalg.lstsq(x, y)[0]
    print(c)

    print(x @ c)

# main()


#  ----SOLUTION-----
print("----intermediate solution----")

def main():
    np.set_printoptions(precision=1)

    x = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600],
            [115, 6, 10, 1, 550]
        ]
    )   

    y = np.array([127900, 222100, 143750, 268000, 460700, 407000])

    c = np.linalg.lstsq(x, y)[0]
    print(c)

    print(x @ c)

main()






'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Write a program that reads cabin details and prices from a CSV file (a standard format for tabular data) and fits a 
# linear regression # model to it. The program should be able to handle any number of data points (cabins) described 
# by any number of features (like size, size of sauna, number of bathrooms, ...).

# You can read a CSV file with the function np.genfromtxt(datafile, skip_header=1). This will return a numpy array 
# that contains the feature data in the columns preceding the last one, and the price data in the last column. The option 
# skip_header=1 just means that the first line in the file is supposed to contain just the column names and shouldn't be 
# included in the actual data.

# The output of the program should be the estimated coefficients and the predicted or "fitted" prices for the same set of 
# cabins used to estimate the parameters. So if you fit the model using data for six cabins with known prices, the 
# program will print out the prices that the model predicts for those six cabins (even if the actual prices are already 
# given in the data).

# Note that here we will not actually only simulate the file input using Python's io.StringIO function that takes an 
# input string and pretends that the contents is coming from a file. In practice, you would just name the input file that 
# contains the data in the same format as the string input below.

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):
    # Please write your code inside this function

    # read the data in and fit it. the values below are placeholder values
    c = np.asarray([])  # coefficients of the linear regression
    x = np.asarray([])  # input data to the linear regression

    print(c)
    print(x @ c)

# simulate reading a file
input_file = StringIO(input_string)
# fit_model(input_file)



# ------SOLUTION-----
print("\n----advanced solution---")

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(data):
    x = []  # input data to the linear regression
    c = []
    y = []    
    input_file = np.genfromtxt(data)

    for i in range(len(input_file)):
        for j in range(len(input_file[i])-1):
            x.append(input_file[i][j])
        y.append(input_file[i][len(input_file[i])-1])

    x = np.array(x)
    x = x.reshape(6,5)

    y = np.array(y)
    
    c = np.linalg.lstsq(x, y)[0]        # coefficients of the linear regression
    print(c)
    print(x @ c)


# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)












# -----------------------------------------------------------------------------------------------------------------------
############
#EXERCISE 14#
############

print('\n\nEXERCISE 14\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# The program estimates the coefficients of a linear regression model (array c) from the following data:
# 	        size 	size of the sauna 	distance to water 	number of indoor bathrooms 	proximity of neighbors 	actual price
# cabin 1 	25 	    2 	                50                  1 	                        500 	                127,900
# cabin 2 	39 	    3 	                10 	                1 	                        1000 	                222,100
# cabin 3 	13 	    2 	                13 	                1 	                        1000 	                143,750
# cabin 4 	82 	    5 	                20 	                2 	                        120 	                268,000
# cabin 5 	130 	6 	                10 	                2 	                        600 	                460,700
# cabin 6 	115 	6 	                10 	                1 	                        550 	                407,000

# Use the predicted coefficients to obtain price estimates for the following two cabins:
# 	        size 	size of the sauna 	distance to water 	number of indoor bathrooms 	proximity of neighbors 	actual price
# cabin 7 	36 	    3 	                15 	                1 	                        850 	                196000
# cabin 8 	75 	    5 	                18 	                2 	                        540 	                290000

# Note that the predicted prices will not be the same as the actual prices (which are given in the above table just for comparison – you 
# won't need them in the exercise).

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    x_train = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600],
            [115, 6, 10, 1, 550 ]
        ]
    )   
    
    y_train = np.array([127900, 222100, 143750, 268000, 460700, 407000])

    # add the feature data for the two new cabins here. note: don't include the price data
    x_test = None

    c = np.linalg.lstsq(x_train, y_train, rcond=-1)[0]

    # this will print the predicted prices for the six cabins in the training data
    # change this so that it predicts the prices of the two new cabins that are not
    # included in the training set

    print(x_train @ c)

# main()



#  -----SOLUTION------
print ("----intermediate solution----")
def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    x_train = np.array([
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600],
            [115, 6, 10, 1, 550 ]
    ])      
    y_train = np.array([127900, 222100, 143750, 268000, 460700, 407000])

    
    x_test = np.array([
        [36, 3, 15, 1, 850],
        [75, 5, 18, 2, 540]
    ])

    c = np.linalg.lstsq(x_train, y_train, rcond=-1)[0]
    print(x_test @ c)

main()






'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Write a program that reads data about one set of cabins (training data), estimates linear regression coefficients based on it, then reads 
# data about another set of cabins (test data), and predicts the prices in it. Note that both data sets contain the actual prices, but the 
# program should ignore the prices in the second set. They are given only for comparison.

# The contents of the sets are as follows.

# training data
# size 	size of the sauna 	distance to water 	number of indoor bathrooms 	proximity of neighbors 	actual price
# 25 	2 	                50 	                1 	                        500 	                127900
# 39 	3 	                10 	                1 	                        1000 	                222100
# 13 	2 	                13 	                1 	                        1000 	                143750
# 82 	5 	                20 	                2 	                        120 	                268000
# 130 	6 	                10 	                2 	                        600 	                460700
# 115 	6 	                10 	                1 	                        550 	                407000

# test data
# size 	size of the sauna 	distance to water 	number of indoor bathrooms 	proximity of neighbors 	actual price
# 36 	3 	                15 	                1 	                        850 	                196000
# 75 	5 	                18 	                2                          	540 	                290000

# You can read the data into the program the same way as in the previous exercise.

# You should then separate the feature and price data that you have just read from the file into two separate arrays names x_train and 
# y_train, so that you can use them as argument to np.linalg.lstsq.

# The program should work even if the number of features used to describe the cabins differs from five (as long as the same number of 
# features are given in each file).

# The output should be the set of coefficients for the linear regression and the predicted prices for the second set of cabins. 

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function

    # read in the training data and separate it to x_train and y_train
     
    # fit a linear regression model to the data and get the coefficients
    c = np.asarray([])

    # read in the test data and separate x_test from it
    x_test = np.asarray([])

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


# main()

# -----SOLUTION-----
print("\n----advanced solution---")

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # ---- DATA TRAIN ----
    data_train = StringIO(train_string)
    data_train = np.genfromtxt(data_train)

    x_train=[]
    y_train=[]

    for i in range(len(data_train)):
        for j in range(len(data_train[i])-1):
            x_train.append(data_train[i][j])
        y_train.append(data_train[i][len(data_train[i])-1])
    
    x_train = np.array(x_train)
    x_train = x_train.reshape(6,5)

    y_train = np.array(y_train)

    c = np.linalg.lstsq(x_train, y_train)[0]    # linear regression coefficients        
    print(c)

    # ---- DATA TEST ----
    data_test = StringIO(test_string)
    data_test = np.genfromtxt(data_test)

    x_test=[]

    for i in range(len(data_test)):
        for j in range(len(data_test[i])-1):
            x_test.append(data_test[i][j])
    
    x_test = np.array(x_test)
    x_test = x_test.reshape(2,5)    

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()