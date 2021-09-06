import numpy as np
import math

#############
#EXERCISE 17#
#############

print('\n\nEXERCISE 17\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Your task is to write a function that calculates the distances (or differences) between a pair of lines in the This 
# Little Piggy rhyme.

# Every row in the list data represents one line in the rhyme.

# When you run the code, you see that the output of the whole program is a list of lists. When your function works correctly, 
# each list will contain the distances between a single row and all the other rows in data.

# Note that the program will compare every row also with itself. In this case – when the compared rows are the same – their 
# distance will be zero.

# You can use the function abs(x-y) to calculate the distance between numbers x and y, where x comes from list row1 and y 
# comes from row2.

# Your program must work with any text, not only with the rhyme This Little Piggy. 

# this data here is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    # fix this function so that it returns 
    # the sum of differences between the occurrences
    # of each word in row1 and row2.
    # you can assume that row1 and row2 are lists with equal length, containing numeric values.
    return 0

def all_pairs(data):
    # this calls the distance function for all the two-row combinations in the data
    # you do not need to change this
    dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    print(dist)

# all_pairs(data)



# -----SOLUTION-----
print("----intermediate solution-----")

# this data here is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    # fix this function so that it returns 
    # the sum of differences between the occurrences
    # of each word in row1 and row2.
    # you can assume that row1 and row2 are lists with equal length, containing numeric values.
    cal = 0
    for x,y in zip(row1, row2):
        cal = cal + abs(x-y)
    return cal

def all_pairs(data):
    # this calls the distance function for all the two-row combinations in the data
    # you do not need to change this
    dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    print(dist)

all_pairs(data)







'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Your task is to write a program that calculates the distances (or differences) between every pair of lines in the This 
# Little Piggy rhyme and finds the most similar pair. Use the Manhattan distance (also called Taxicab distance) as your 
# distance metric.

# You can start by building a numpy array to store all the distances. Notice that the diagonal elements in the array 
# (elements at positions [i, j] with i=j) will be equal to zero. This happens because the program will compare every row 
# also with itself. To avoid selecting those elements, you can assign the value np.inf (the maximum possible floating point 
# value). To do this, it's necessary to make sure the type of the array is float.

# A quick way to get the index of the element with the lowest value in a 2D array (or in fact, any dimension) is by the 
# function

# np.unravel_index(np.argmin(dist), dist.shape))

# where dist is the 2D array. This will return the index as a list of length two. If you're curious, here's an intuitive 
# explanation of the function, and here's its documentation.


data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    print(np.unravel_index(np.argmin(dist), dist.shape))

# find_nearest_pair(data)



#  ----SOLUTION----
print("\n---ADVANCED solution----")

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance (row1, row2):
    cal = 0
    for x,y in zip(row1, row2):
        cal = cal + abs(x-y)
    
    if cal == 0: 
        return np.inf
    else:
        return cal


def find_nearest_pair(data):
    dist = np.array([[distance(sent1, sent2) for sent1 in data] for sent2 in data])
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)







# ------------------------------------------------------------------------------------------------------------------
print('\n\nEXERCISE 18\n')
'''**************************************************************'''
'''************************ INTERMEDIATE ************************'''
'''**************************************************************'''
# Modify the following program to print out the tf-idf values for each document and each word. The following code 
# calculates the tf and df values, so you'll just need to combine them according to the correct formula. There are three 
# documents (sentences) and a total of eight terms (unique words), so the output should be three lists of eight tf-idf 
# values each. 

# DATA BLOCK

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''


def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            tfidf.append(None) 

        print(tfidf)

# main(text)



# -----SOLUTION-----
print("----intermediate solution-----")

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    print("TF: ", tf)
    print("DF: ", df)

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            value = tf[word][doc_index] * math.log(1/df[word], 10)
            tfidf.append(value) 

        print(tfidf)

main(text)









'''**************************************************************'''
'''************************ ADVANCED ****************************'''
'''**************************************************************'''
# Let's combine two tasks: finding the most similar pair of lines and the tf-idf representation.

# Write a program that uses the tf-idf vectors to find the most similar pair of lines in a given data set. You can test 
# your solution with the example text below. Note, however, that your solution will be tested on other data sets too, so 
# make sure you don't make use of any special properties of the example data (like there being four lines of text).

# This exercise requires a bit more work than average but you should be able to benefit from what you have done in the 
# previous exercises.

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    pass
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.


# main(text)


# ---- SOLUTION ----
print("\n---ADVANCED solution----")



text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def distance (row1, row2):
    cal = 0
    for x,y in zip(row1, row2):
        cal = cal + abs(x-y)
    
    if cal == 0: 
        return np.inf
    else:
        return cal

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    vocabulary = list(set(text.lower().split()))
    N = len(docs)

    df = {}
    tf = {}
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/N
    
    # print("TF: ", tf)
    # print("\nDF: ", df)

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    tfidf = []
    for doc_index, doc in enumerate(docs):    
        tfidf.append([])    
        for word in vocabulary:
            value = tf[word][doc_index] * math.log(1/df[word], 10)
            tfidf[doc_index].append(value)
        # print("\nTF-IDF: ",tfidf)
        

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    dist = np.array([[distance(sent1, sent2) for sent1 in tfidf] for sent2 in tfidf])
    print(np.unravel_index(np.argmin(dist), dist.shape))


main(text)