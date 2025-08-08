import numpy as np
rev_q1 = np.array([1, 2, 3, 4, 5])
print(rev_q1.ndim) #Dimensions of the array
rev = np.array([[1, 2, 3], [4, 5, 6]])
print(rev.ndim) #Dimensions of the array
print(rev)
# Locate the revenue of second quarter, first month
print(rev[1,0])
# Update the revenue of second quarter, first month
rev[1,0] = 10
print(rev[1,0])
# Data type of the array
print(rev.dtype)
# Specify the data type of the array
rev = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
# Size occupied by each element in bytes
print(rev.itemsize)
# Total size of elements
print(rev.size)
# Number of rows and columns
print(rev.shape)
# Sort the array
print(np.sort(rev))
# Create an array of zeros
zeros = np.zeros((2, 3))
print(zeros)
# Create an array of ones
ones = np.ones((2, 3))
print(ones)
# Create an array of a range of numbers
range4 = np.arange(4)
print(range4)
# Create an array of a range between specific numbers
range_10 =  np.arange(10,20)
print(range_10)
# Create an array of a range with a specific step (distance between numbers)
range_10_step = np.arange(10, 20, 2)
print(range_10_step)
# Create an array of evenly spaced numbers over a specified interval
linspace_1 = np.linspace(0, 1, 5)  # 5 numbers between 0 and 1
print(linspace_1)
# make a single list
print(rev.ravel())
# flatten the array, returns a copy
print(rev.flatten())
# reshape the array, has to be compatible with the original size
reshaped_rev = rev.reshape(3, 2)  # Reshape to 3 rows and 2 columns
print(reshaped_rev)
# minimum and maximum values
print(rev.min())
print(rev.max())
# sum of a quarter
print(rev.sum(axis=1)) # Sum across rows
print(rev.sum(axis=0))  # sum across columns
# itearate through the array
for row in rev:
    for value in row:
        print(value)

for row in rev:
    print(row)

# square each element in the array
print(rev)
print(np.sqrt(rev))
# standard deviation
print(np.std(rev))  # Standard deviation

