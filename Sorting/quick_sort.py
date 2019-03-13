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

def quick_sort(arr):
    quick_sort_help(arr, 0, len(arr) - 1)

def quick_sort_help(arr, first, last):
    if first < last:
        split_point = partition(arr, first, last)

        quick_sort_help(arr, first, split_point - 1)
        quick_sort_help(arr, split_point + 1, last)
        
def partition(arr, first, last):
    pivot_value = arr[first]    # to assist splitting the array
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivot_value:
            leftmark += 1
        while leftmark <= rightmark and arr[rightmark] >= pivot_value:
            rightmark += 1
        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
            
        temp = arr[first]
        arr[first] = arr[rightmark]
        arr[rightmark] = temp

    return rightmark
        
#-----------------------------------#-----------------------------------
import statistics
# def median(a, first, last, middle):
#     if a[first] < a[last]:
#         return first if a[middle] < a[first] else middle if a[middle] < a[last] else last
#     else:
#         return last if a[middle] < a[last] else middle if a[middle] < a[first] else first


def quick_sort_median(lst):
    quick_sort_median_helper(lst,0,len(lst) - 1)
    
def quick_sort_median_helper(lst,first,last):
    if first < last:
        splitpoint = partition_median(lst,first,last)
        quick_sort_median_helper(lst,first,splitpoint - 1)
        quick_sort_median_helper(lst,splitpoint + 1,last)
    


def partition_median(lst,first,last):
    pivotindex = statistics.median([first, last, (first + last) // 2])
    lst[first], lst[pivotindex] = lst[pivotindex], lst[first]
    pivotvalue = lst[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and lst[leftmark] <= pivotvalue:
            leftmark += 1
        while lst[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = lst[leftmark]
            lst[leftmark] = lst[rightmark]
            lst[rightmark] = temp

    temp = lst[first]
    lst[first] = lst[rightmark]
    lst[rightmark] = temp

    return rightmark

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
