# -------------------------------
# NUMPY (Numerical Python)
# -------------------------------

import numpy as np
import time
from numpy import random
from scipy import stats

# -------------------------------
# 1. BASIC ARRAY CREATION
# -------------------------------
num = np.array([10, 20, 30, 40, 50])
print(type(num))  # <class 'numpy.ndarray'>
print(num)        # [10 20 30 40 50]

# -------------------------------
# 2. NUMPY VS PYTHON LIST
# -------------------------------
# Sum using list
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total += n
print(total)      # 15

# Sum using numpy
numbers = np.array([1, 2, 3, 4, 5])
print(np.sum(numbers))  # 15

# -------------------------------
# 3. EXECUTION TIME COMPARISON
# -------------------------------
numbers = list(range(1, 10000))
n = 0
start_time = time.time()
for i in numbers:
    n += i
end_time = time.time()
print("Total:", n)  # 49995000
print(f"Execution Time: {end_time - start_time:.4f} seconds")  

# -------------------------------
# 4. ARRAY SHAPE
# -------------------------------
num = np.array([10, 20, 30, 40, 50])
print(num.shape)  # (5,)  -> 1D array

num2d = np.array([[1, 2], [3, 4], [5, 6]])
print(num2d)
# [[1 2]
#  [3 4]
#  [5 6]]
print(num2d.shape)  # (3,2) -> 3 rows, 2 columns

# -------------------------------
# 5. INDEXING & SLICING
# -------------------------------
arr = np.array([10,20,30,40,50,60,70,80,90])
print(arr[2])      # 30
print(arr[-1])     # 90
print(arr[2:7])    # [30 40 50 60 70]
print(arr[::-1])   # [90 80 70 60 50 40 30 20 10]
print(arr[2:7:2])  # [30 50 70]

num2d = np.array([[1,2],[3,4],[5,6]])
print(num2d[0,1])  # 2
print(num2d[:,1])  # [2 4 6] -> 2nd column
print(num2d[2,:])  # [5 6] -> last row

# -------------------------------
# 6. DATA TYPES
# -------------------------------
num = np.array([10,20,30,40])
print(num.dtype)  # int64

num = np.array([10.12,20.4,30.60,40])
print(num.dtype)  # float64

num = np.array([True,False,False])
print(num.dtype)  # bool

# -------------------------------
# 7. COPY VS VIEW
# -------------------------------
org_arr = np.array([1,2,3,4,5])
copied_arr = org_arr.copy()  # independent copy
copied_arr[0] = 100
print(copied_arr)  # [100 2 3 4 5]
print(org_arr)     # [1 2 3 4 5]

view_arr = org_arr.view()  # shares memory
view_arr[0] = 200
print(view_arr)  # [200 2 3 4 5]
print(org_arr)   # [200 2 3 4 5]

# -------------------------------
# 8. RESHAPING ARRAYS
# -------------------------------
arr = np.arange(1,13)
print(arr.shape)  # (12,)
twod = arr.reshape(3,4)
print(twod)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# using -1 or flatten
twod = np.array([[1,2],[3,4],[5,6]])
ar = twod.reshape(-1)
print(ar)  # [1 2 3 4 5 6]
print(twod.flatten())  # [1 2 3 4 5 6]

# newaxis
arr = np.array([1,2,3,4,5])
print(arr[:, np.newaxis])
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]]

# -------------------------------
# 9. CONCATENATION & SPLIT
# -------------------------------
num1 = np.array([1,2,3,4])
num2 = np.array([5,6,7,8])
print(np.concatenate((num1,num2)))  # [1 2 3 4 5 6 7 8]

num = np.arange(1,11)
print(np.array_split(num, 3))  # [array([1,2,3,4]), array([5,6,7]), array([8,9,10])]

# -------------------------------
# 10. SORTING
# -------------------------------
prices = np.array([50,67,98,23,56,12,55,99])
print(np.sort(prices)[::-1])  # [99 98 67 56 55 50 23 12]

# -------------------------------
# 11. FILTERING & SEARCHING
# -------------------------------
num = np.array([1,3,7,3,5,9,6,2,10])
print(num[num>=5])  # [7 5 9 6 10]

# using np.where
res = np.where(num>=5)
print(res)  # (array([2, 4, 5, 6, 8]),)

arr = np.array([10,32,30,50,20,82,91,45])
print(np.where(arr==30))  # (array([2]),)
print(np.where(arr%2==0)) # (array([0, 1, 2, 4, 5]),)
print(np.where(arr>40, arr*2, arr))  # [10 32 30 100 20 164 182 90]

# -------------------------------
# 12. RANDOM NUMBERS
# -------------------------------
x = random.randint(100)
print(x)  # random int 0-99
print(random.rand())  # random float 0-1
print(random.choice([3,4,5,6]))  # random choice

# -------------------------------
# 13. ZEROS, SUM, MEAN, MODE
# -------------------------------
num = np.zeros(12)
print(num)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

x = np.random.randint(0,54,12)
print(x)
print(np.sum(x))
print(np.mean(x))
print(stats.mode(x))  # mode

# -------------------------------
# 14. UNIQUE & ARGSORT
# -------------------------------
arr = [1,2,3,4,2,3,4,5,8,6,5,4,3,9,8,7,4,3,3,5,6]
print(np.unique(arr))  # [1 2 3 4 5 6 7 8 9]

arr = np.array([1,2,3,4,1,2,1,1,1,5,6,7,5,9,10,11,8,6,5])
uv, i = np.unique(arr, return_index=True)
print(uv)  # [ 1 2 3 4 5 6 7 8 9 10 11]
print(i)   # first occurrence indices
print(uv[np.argsort(i)])  # restore original order

# -------------------------------
# 15. ARANGE
# -------------------------------
print(np.arange(11))      # [0 1 2 3 4 5 6 7 8 9 10]
print(np.arange(1,11))    # [1 2 3 4 5 6 7 8 9 10]
print(np.arange(1,11,3))  # [1 4 7 10]

# -------------------------------
# 16. BROADCASTING
# -------------------------------
arr1 = np.array([4,5,7,8])
arr2 = np.array([8,1,3,4])
print(arr1 + arr2)  # [12 6 10 12]

arr2 = np.array([8])
print(arr1 + arr2)  # [12 13 15 16]