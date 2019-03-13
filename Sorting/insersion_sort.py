#-----------------------------------
#|---------------------------------|
#|       Insersion Sort:           |
#|---------------------------------|
#-----------------------------------

# Description: 
#   Select the first element in the unsorted array, and insert it in the sorted array(the section of the array before that element) in the first round, index 1 

# Python code:

#-----------------------------------#-----------------------------------
def insertion_sort(arr): 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1   # j is the last index of sorted array
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
 #-----------------------------------#-----------------------------------
       
# Time Complexity: 
#   O(n^2) as there are two nested loops.

# Boundary Cases: 
#   Insertion sort takes maximum time to sort if elements are sorted in reverse order. 
#   And it takes minimum time (Order of n) when elements are already sorted.

# Uses: 
# Insertion sort is used when number of elements is small. 
# It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.

# Auxiliary Space: O(1): 
#   Selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

# In Place : 
#   Yes, it does not require extra space.

# Stable: Yes

# Demo.
#   0. arr[] = 64 25 12 22 11
#   1. arr[] = 25 64 12 22 11
#   2. arr[] = 12 25 64 22 11
#   3. arr[] = 12 22 25 64 11
#   4. arr[] = 11 12 22 25 64
