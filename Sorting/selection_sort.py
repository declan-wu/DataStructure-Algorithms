#-----------------------------------
#|---------------------------------|
#|       Selection Sort:           |
#|---------------------------------|
#-----------------------------------
# Description: 
#   The selection sort algorithm sorts an array by repeatedly finding the minimum element 
#   (considering ascending order) from unsorted part and putting it at the beginning. 

# Python code:

#-----------------------------------#----------------------------------- 
def  selection_sort(arr): 
    for i in range(len(arr)): 
        min_idx = i   # index of minimum element in remaining unsorted array
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j
        # Swap the found minimum element with the first element         
        arr[i] , arr[min_idx] = arr[min_idx], arr[i] 
#-----------------------------------#----------------------------------- 
        
# Time Complexity: 
#   O(n^2) as there are two nested loops.

# Auxiliary Space: O(1): 
#   Selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

# In Place : 
#   Yes, it does not require extra space.

# Demo.
#   0. arr[] = 64 25 12 22 11
#   1. arr[] = 11 64 25 12 22
#   2. arr[] = 11 12 64 25 22
#   3. arr[] = 11 12 22 64 25
#   4. arr[] = 11 12 22 25 64
#   5. arr[] = 11 12 22 25 64
