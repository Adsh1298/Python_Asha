import numpy as np
from scipy import stats
# def perform_array_operations(arr):
#     print(arr)
#     print(type(arr))
#     print(arr.shape)
# #Shape property give a tuple of integers representing size and no of elements in
# # that dimension
# #How to create a 1-D Array using numpy:
# arr1 = np.array([1,2,3,4,5,6,7,8,9])
# mul_arr=np.array([[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]])
# print("########################For Single Dimensional Array #####################")
# perform_array_operations(arr1)
# print("########################For Multiple Dimensional Array ####################")
# perform_array_operations(mul_arr)
# print("##################Creating Multiple Dimensional Array "
#       "####################")
# mul_arr=np.array([1,2,3,4,5], ndmin=3)
# perform_array_operations(mul_arr)
# print("########################Arrays of values ####################")
# ones=np.ones((2,4)) #2x4 with values set to 1.
# print(ones)
#
# range_arr = np.arange(10, 30, 2)
# print(range_arr)
#
# rand_arr=np.random.rand(4, 5)
# print(rand_arr*10) #random gives a random b/w 0 and 1.
#
# def print_info_array(arr):
#     print("Array:\n",arr)
#     print("Shape:\n",arr.shape)
#     print("No of dimensions:\n",arr.ndim)
#     print("Size(No of elements): ", arr.size)
#     print("Item Size: (Byte size)", arr.itemsize)
#     arr=np.array([[1,2,3,4,5],[5,6,7,8,9]])
# #     print_info_array(arr)
# # arr2=np.array([1,2,3,4,5],[5,6,7,8])
# # print("\n2 D Array:\n",arr2)
# #
# # arr3=np.array([6,7,8,9,10])
# # sum_arr==arr+arr3
# # print(sum_arr)
# # mul_arr=arr*arr3
# # print(mul_arr)
# #
# # avg=np.mean(mul_arr)
# # print("\nMean of arr:", avg)
# # print("\nStd Deviation:",np.std(mul_arr))
# # print("No of dimensions:",arr2.ndim)
# # print("No of elements:",arr2.size)
# ##########################Indexing feature of arrays###############################
# arr=[1,2,3,4,5,6,7,8,9,10]
# single_element=arr[1]
# print(single_element)
# first_three_elements=arr[1:4]
# print(first_three_elements)
# print(arr[-2])
#
# print(arr[:5])
# print(arr[::2])
# print(arr[::3])
# print(arr[::-1])
# # a=arr.copy()
# # print(a)
# # b=arr.reverse()
# # print(b)
#
# print(arr[-4:-8:-2])
# sqr_arr=[x**2 for x in arr]# Exponential multiplication of every index
# print(sqr_arr)
#####################Vector operation############################
arr1=np.array([1,2,3,4,5])
arr2 = arr1*10
print(f"Addition:",arr1+arr2)
print(f"Subtraction:",arr1-arr2)
print(f"Multiplication:",arr1*arr2)
print(f"Division:",arr1/arr2)
########################Common Global function#################################
print(np.sqrt(arr1))
print(np.sin(arr1))
print(np.cos(arr1))
print(np.log(arr1))
print(np.cos(arr1))
print(arr1[(arr1>=1) & (arr1<=10)])
###################Statical functions#######################
arr1=np.array([1,2,3,4,5])
mean=np.mean(arr1)
median_value=np.median(arr1)
std_deviation=np.std(arr1)
variance = np.var(arr1)
mode_value = stats.mode(arr1)

print(f"Mean:",mean)
print(f"Median:",median_value)
print(f"Standard Deviation:",std_deviation)#standarc measure of how data is
# clustered around the mean
print(f"Variance:",variance)#The mean of the sqaures subtracted by the square of
# the mean
print(f"Mode:",mode_value)
##########################Sorting function###############################
arr1 = np.array([3,4,2,5,1,6,9,8])
sorted_arr=np.sort(arr1)#[::-1]
sorted_indices=np.argsort(arr1) #Sorting the values and return the indices
print(sorted_arr,sorted_indices)

######################Unique values##############################
arr1 = np.array([3,4,2,5,1,6,9,8])
unique_values = np.unique(arr1)
#unique_counts=np.unique(arr1,return_counts=True)
values,count = np.unique(arr1,return_counts=True)

print("unique values:",unique_values)
#print("Unique Counts:",unique_counts)
#Histogram
for value,count in zip(unique_values,count):
    print(f"Value {value} appears {count} no of times")












