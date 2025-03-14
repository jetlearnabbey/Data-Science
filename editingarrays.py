import numpy as np
import sys

'''list = [1, 2, 3, 4, 5]

array = np.array(list)

print(list)

print(array)

print("list ",sys.getsizeof(list))

print("array ",array.nbytes)

print(type(array))

print(type(list))
'''
#14/03/25

#Specifing the data type

'''ara1 = np.array([1, 2, 3, 4, 5],dtype="f")
print(ara1)

#Create a multidirectional array

ara2 = np.array([[1,2,4,5] , [3,4,5,6]])

#print dimension of ara

print(ara2.ndim)
#print the shape of ara

print(ara2.shape)

#give an array of numbers in a range

arrayrange = np.arange(1,10,2) 
print(arrayrange)

#give an random arragment of numbers

randarrage = np.random.permutation(np.arange(1,10) )
print(randarrage)

#get a random number using numpy

randnumber = np.random.randint(1,100)
print(randnumber)

#get a random array of a specified dimension

randarray = np.random.rand(2,4)
print(randarray)


#reshape a linear array to a specified dimension

randomarray = np.arange(1,10).reshape(3,3)
print(randomarray)

randomarray = np.arange(1,37).reshape(36,1)
print(randomarray)

#sorting an array

print(np.sort(randarrage))'''

#create a numpy array of zeros

print(np.zeros(5))

#create a numpy array of ones

print(np.ones(5))

print(np.ones((4,2,2),dtype="int32"))
