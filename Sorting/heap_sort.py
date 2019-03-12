#-----------------------------------
#|---------------------------------|
#|          Heap Sort:             |
#|---------------------------------|
#-----------------------------------

# Binary heap:
#     1. It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). 
#     2. A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all keys present in Binary Heap.

# How is Binary Heap represented?
#     1. The root element will be at Arr[0]
#     2. Arr[(i-1)/2] Returns the parent node
#     3. Arr[(2*i)+1] Returns the left child node
#     4. Arr[(2*i)+2] Returns the right child node 

# Python code:

#-----------------------------------#-----------------------------------
# This is a min priority queue implementation
def left_child_idx(index):
    return 2 * index + 1
def right_child_idx(index):
    return 2 * index + 2
def parent_idx(index):
    return (index - 1) // 2

def has_parent(index):
    return parent_idx(index) >= 0
def has_left_child(arr, index):
    return right_child_idx(index) < len(arr)
def has_right_child(arr, index):
    return left_child_idx(index) < len(arr)

def left_child(arr, index):
    return arr[left_child_idx(index)]
def right_child(arr, index):
    return arr[right_child_idx(index)]
def parent(arr, index):
    return arr[parent_idx(index)]

def swap(index_1, index_2, arr):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]

def heapify_up(arr, index):
    # swim up the last element in the array
    while has_parent(index) and arr[index] < parent(arr, index):
        swap(index, parent_idx(index), arr)
        index = parent_idx(index)

def smaller_child_idx(arr, index):
    if has_left_child(arr, index):
        smaller_idx = left_child_idx(index)
    if has_right_child(arr, index) and right_child(arr, index) < left_child(arr, index):
        smaller_idx = right_child_idx(index)
    return smaller_idx

def heapify_down(arr, index):
    # sink down the root element in the array
    while has_left_child(arr, index) and arr[index] > arr[smaller_child_idx(arr, index)]:
        smaller_idx = smaller_child_idx(arr, index)
        swap(index, smaller_idx, arr)
        index = smaller_idx

def build(arr):
    for i in range(len(arr) // 2, -1, -1): 
        heapify_down(arr, i)

# NOT working, need a third argument length for heapify
def heap_sort(arr):
    for i in range(1, len(arr)):
        swap(0, len(arr) - i, arr)
        b = arr[:len(arr) - i]
        heapify_down(b, 0)
        arr = b + arr[len(arr) - i:]
     
#-----------------------------------

# Time Complexity: 
#     Time complexity of heapify is O(nLogn). 
#     Time complexity of createAndBuildHeap() is O(n).
#     Overall time complexity of Heap Sort is O(nLogn).

# Uses:
#     Heap sort algorithm has limited uses because Quicksort and Mergesort are better in practice. Nevertheless, the Heap data structure itself is enormously used

# In Place : 
#   Yes, it does not require extra space.

# Stable: No
