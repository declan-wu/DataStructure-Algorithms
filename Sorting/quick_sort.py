#-----------------------------------
#|---------------------------------|
#|        Quick Sort:              |
#|---------------------------------|
#-----------------------------------

# Description: 
#   It picks an element as pivot and partitions the given array around the picked pivot. 

# Python code:

#-----------------------------------#-----------------------------------
# This quick sort uses beginning element as a pivot
def quicksort(array):
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, start, stop):
    if start < stop:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)
        
#-----------------------------------#-----------------------------------
# INCOMPLETE!!!
# This quick sort uses middle element as a pivot
def quick_sort(arr): 
    mid_idx = len(arr) // 2     # as the pivot index
    pivot = arr[mid_idx]
    i, j = 0, len(arr)-1     # i is start and j is end

    while i <= j:

        while arr[i] < pivot and i < mid_idx:
            i += 1
        while arr[j] > pivot and j > mid_idx:
            j -= 1

        # meaning we got to a point where an element on the left is greater than pivot
        # or a point on the right is less than pivot, or one/both side is aleady in correct position
        if i < j and j == mid_idx:
            # meaning the right side is in order
            arr[i], arr[j] = arr[j], arr[i]    
            i += 1
            j -= 1
            mid_idx = j
            pivot = arr[mid_idx]

        if i < j and i == mid_idx:
            # meaning the left side is in order
            
        if i == j and i == mid_idx:
            return i
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]    
            i += 1
            j -= 1
#-----------------------------------#-----------------------------------
            
# Time Complexity: 
    # Big Theta (n2) - Worst Case: 
    #     The worst case occurs when the partition process always picks greatest or smallest element as pivot. 
    # Big Theta (NLgN) - Best Case: 
    #     The best case occurs when the partition process always picks the middle element as pivot.
    # Big Oh (NLgN) - Average Case:
    #     Consider all possible permutation of array and calculate time taken by every permutation. 

# Uses:
    # QuickSort is faster in practice, because its inner loop can be efficiently implemented on most architectures, 
    # and in most real-world data. QuickSort can be implemented in different ways by changing the choice of pivot, 
    # so that the worst case rarely occurs for a given type of data. 
    # However, merge sort is generally considered better when data is huge and stored in external storage.

# Auxiliary Space: O(n)

# In Place : No

# Stable: 
#   The default implementation is not stable. 
