# input tuple
inputTuple = (10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7)
# printing input tuple
print ("Input Tuple:", inputTuple)
# Giving the Number of sub-tuples required
n = 3
resultTuple = tuple(inputTuple[i:i + n] for i in range(0, len(inputTuple), n))
print ("Splitting the input tuple into the group of 4-tuples with 3 elements in each:", resultTuple)