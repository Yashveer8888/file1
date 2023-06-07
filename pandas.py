# what is pandas?
'''Python Pandas is defined as an open-source library that provides high-performance data 
manipulation in Python. This tutorial is designed for both beginners and professionals.'''

# Python Pandas Data Structure
'''The Pandas provides two data structures for processing the data, i.e., Series and DataFrame,
which are discussed below:'''

# 1) Series
'''It is defined as a one-dimensional array that is capable of storing various data types. 
The row labels of series are called the index. We can easily convert the list, tuple, and 
dictionary into series using "series' method. A Series cannot contain multiple columns.
It has one parameter:
Data: It can be any list, dictionary, or scalar value.'''

# Creating Series from Array:
import pandas as pd  
import numpy as np  
info = np.array(['P','a','n','d','a','s'])  
a = pd.Series(info)  
print(a) 
output
0   P
1   a
2   n
3   d
4   a
5   s
dtype: object
  
# 2) DataFrame
'''It is a widely used data structure of pandas and works with a two-dimensional array with 
labeled axes (rows and columns). DataFrame is defined as a standard way to store data and has
two different indexes, i.e., row index and column index. It consists of the following 
properties:
The columns can be heterogeneous types like int, bool, and so on.
It can be seen as a dictionary of Series structure where both the rows and columns are indexed.
It is denoted as "columns" in case of columns and "index" in case of rows.'''

# Create a DataFrame using List:
import pandas as pd    
x = ['Python', 'Pandas']   
df = pd.DataFrame(x)  
print(df)  
output
     0
0   Python
1   Pandas

# Python Pandas Series
data: It can be any list, dictionary, or scalar value.
index: The value of the index should be unique and hashable. It must be of the same length as data.
  If we do not pass any index, default np.arrange(n) will be used.
dtype: It refers to the data type of series.
copy: It is used for copying the data.
  
# Create an empty Series
import pandas as pd  
x = pd.Series()  
print(x) output-->  Series([], dtype: float64)

# Creating a Series using inputs:
# Creating Series from Array:
info = np.array(['P','a','n','d','a','s'])  
a = pd.Series(info)  
print(a) 
output
0    P
1    a
2    n
3    d
4    a
5    s
dtype: object

# Create a Series from dict 
info = {'x' : 0., 'y' : 1., 'z' : 2.}  
a = pd.Series(info)  
print(a)  
output
x     0.0
y     1.0
z     2.0
dtype: float64

# Create a Series using Scalar:
x = pd.Series(4, index=[0, 1, 2, 3])  
print(x)  
output
0      4
1      4
2      4
3      4
dtype: int64

# Accessing data from series with Position:
x = pd.Series([1,2,3],index = ['a','b','c'])  
print(x[0])  output--> 1
print(x['b'])  output--> 2

# Series object attributes
Series.index:	Defines the index of the Series.
Series.shape:	It returns a tuple of shape of the data.
Series.dtype:	It returns the data type of the data.
Series.size:	It returns the size of the data.
Series.empty:	It returns True if Series object is empty, otherwise returns false.
Series.hasnans:	It returns True if there are any NaN values, otherwise returns false.
Series.nbytes:	It returns the number of bytes in the data.
Series.ndim:	It returns the number of dimensions in the data.
Series.itemsize:	It returns the size of the datatype of item.
  
# 




  
