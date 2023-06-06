# what is numpy
'''NumPy stands for numeric python which is a python package for the computation and processing of the multidimensional and single dimensional array elements.'''
# Creating a ndarray object
''' use numpy module'''
import numpy
arr=numpy.arry
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)  

# parameters
1	object: It represents the collection object. It can be a list, tuple, dictionary, set, etc.
2	dtype:	We can change the data type of the array elements by changing this option to the specified type. The default is none.
3	copy:	It is optional. By default, it is true which means the object is copied.
4	order:	There can be 3 possible values assigned to this option. It can be C (column order), R (row order), or A (any)
5	subok:	The returned array will be base class array by default. We can change this to make the subclasses passes through by setting this option to true.
6	ndmin:	It represents the minimum dimensions of the resultant array.
  
a = numpy.array([1, 2, 3])
print(a) output--> [1,2,3]
print(type(a)) output--> <class 'numpy.ndarray'>

a = numpy.array([[1, 2, 3], [4, 5, 6]])  
print(a) output--> [[1, 2, 3]
                    [4, 5, 6]]

a = numpy.array([1, 3, 5, 7], complex)  
print(a) output--> [1.+0.j 3.+0.j 5.+0.j 7.+0.j]

# Finding the dimensions of the Array
arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])  
print(arr.ndim) output--> 2

# Higher dimensional array
import numpy
b=numpy.array([1,2,3,4,5],ndmin=6)
print(b)
print(b.ndim)
output
[[[[[[ 1 2 3 4 5]]]]]]
6


# Finding the size of each array element
a = np.array([[1,2,3]])  
print("Each item contains",a.itemsize,"bytes.") output--> Each item contains 8 bytes.

# Finding the data type of each array item
a = np.array([[1,2,3]])  
print("Each item is of the type",a.dtype)  output--> Each item is of the type int64

# Finding the shape and size of the array
a = np.array([[1,2,3,4,5,6,7]])  
print("Array Size:",a.size)  output--> Array Size: 7
print("Shape:",a.shape)  output--> Shape: (1,7)

# Reshaping the array objects
a = np.array([[1,2],[3,4],[5,6]])  
print("printing the original array..")  
print(a)  output--> [[1,2]
                     [3,4]
                     [5,6]]
a=a.reshape(2,3)  
print("printing the reshaped array..")  
print(a)  output--> [[1 2 3]
                     [4 5 6]]

# Slicing in the Array
a = np.array([[1,2],[3,4],[5,6]])  
print(a[0,1]) output--> 2
print(a[2,0]) output--> 5
  
b=numpy.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print(b[1]) output--> [[1 2 3 4]
                       [5 6 7 8]]
print(b[0,0]) output--> [1 2 3 4]
print(b[0,1,0]) output--> 5

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2]) output--> [[ 1  2  3  4  5]
                           [ 6  7  8  9 10]]
print(arr[1,1:5]) output--> [ 7  8  9 10]
print(arr[0:2,3]) output--> [4 9]
print(arr[0,1:4:2]) output--> [2 4]
print(arr[1:3,2:4]) output--> [[8 9]]    

# Linspace
a=np.linspace(5,15,10)
print(a) output--> [ 5.          6.11111111  7.22222222  8.33333333  9.44444444 10.55555556
 11.66666667 12.77777778 13.88888889 15.        ]

# Finding the maximum, minimum, and sum of the array elements
a = np.array([1 2 3 10 15 4])  
print(a) output--> [1,2,3,10,15,4]
print(a.max()) output--> 15
print(a.min()) output--> 1
print(a.sum()) output--> 35

# NumPy Array Axis
a = np.array([[1,2,30],[10,15,4]])  
print(a) output--> [[1 2 30]
                    [10 15 4]]
print(a.max(axis = 0)) output--> [10 15 4]
print(a.min(axis = 1))  output--> [1 4]
print(a.sum(axis = 1))  output--> [33 29]
print(a.sum(axis = 0))  output--> [11 17 34]

# Finding square-(sqrt) root and standard-(std) deviation
a = np.array([[1,2,30],[10,15,4]])  
print(np.sqrt(a)) output--> [[1.         1.41421356 5.47722558]
                             [3.16227766 3.87298335 2.        ]]
print(np.std(a))  output--> 10.044346115546242

# Arithmetic operations on the array
a = np.array([[1,2,30],[10,15,4]])  
b = np.array([[1,2,3],[12, 19, 29]])  
print(a+b) output--> [[ 2  4 33]
                      [22 34 33]]
print(a*b) output--> [[  1   4  90]
                      [120 285 116]]
print(a/b) output--> [[ 1.          1.         10.        ]
                      [ 0.83333333  0.78947368  0.13793103]]
print(a**b)  output--> [[         1          4      27000]
                        [-727379968  198698543          0]]

# Array Concatenation vertically-(vstack) & horizontally-(hstack)
a = np.array([[1,2,30],[10,15,4]])  
b = np.array([[1,2,3],[12, 19, 29]])  
print("Arrays vertically concatenated\n",np.vstack((a,b)))
output --> Arrays vertically concatenated
 [[ 1  2 30]
 [10 15  4]
 [ 1  2  3]
 [12 19 29]]
print("Arrays horizontally concatenated\n",np.hstack((a,b)))  
output--> Arrays horizontally concatenated
 [[ 1  2 30  1  2  3]
 [10 15  4 12 19 29]]

# NumPy Datatypes
1	bool_:	It represents the boolean value indicating true or false. It is stored as a byte.
2	int_:	It is the default type of integer. It is identical to long type in C that contains 64 bit or 32-bit integer.
3	intc:	It is similar to the C integer (c int) as it represents 32 or 64-bit int.
4	intp:	It represents the integers which are used for indexing.
5	int8:	It is the 8-bit integer identical to a byte. The range of the value is -128 to 127.
6	int16:	It is the 2-byte (16-bit) integer. The range is -32768 to 32767.
7	int32:	It is the 4-byte (32-bit) integer. The range is -2147483648 to 2147483647.
8	int64:	It is the 8-byte (64-bit) integer. The range is -9223372036854775808 to 9223372036854775807.
9	uint8:	It is the 1-byte (8-bit) unsigned integer.
10 uint16:	It is the 2-byte (16-bit) unsigned integer.
11 uint32:	It is the 4-byte (32-bit) unsigned integer.
12 uint64:	It is the 8 bytes (64-bit) unsigned integer.
13 float_:	It is identical to float64.
14 float16:	It is the half-precision float. 5 bits are reserved for the exponent. 10 bits are reserved for mantissa, and 1 bit is reserved for the sign.
15 float32:	It is a single precision float. 8 bits are reserved for the exponent, 23 bits are reserved for mantissa, and 1 bit is reserved for the sign.
16 float64:	It is the double precision float. 11 bits are reserved for the exponent, 52 bits are reserved for mantissa, 1 bit is used for the sign.
17 complex_:	It is identical to complex128.
18 complex64:	It is used to represent the complex number where real and imaginary part shares 32 bits each.
19 complex128:	It is used to represent the complex number where real and imaginary part shares 64 bits each.

# NumPy dtype
numpy.dtype(object, align, copy)  

Object: It represents the object which is to be converted to the data type.
Align: It can be set to any boolean value. If true, then it adds extra padding to make it equivalent to a C struct.
Copy: It creates another copy of the dtype object.
  
d = np.dtype(np.int32)  
print(d) output--> int32













