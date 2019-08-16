# a priority queue acts like a queue in that you dequeue an item by removing it from the front
# however, in a priority queue the logical order of items inside a queue is determined by their priority
# highest priority item are at the front of the queue an dthe lowest priority items are at the back. When you enqueue an item on a priority queue, the new item may move all the way to the front

# The classical way to implement a priority queue is using a data structure called a binary heap.
# Binary Heap will allow us both enqueue and dequeue items in O(Ln N) time.


class BinaryHeap:
    def __init__(self):
        # note that we have a single 0 on the list, so that the first element would be index 1, and its left child would be at index 2 * i, and right child would be at index 2 * i + 1; and it's good for integer division purpose we are going use later on
        self.heapList = [0]
        self.curerntSize = 0

    def percUp(self, i):
        # while that element at index i has a parent
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                # swap the two elements
                self.heapList[i //
                              2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.curerntSize = self.curerntSize + 1
        self.percUp(self.curerntSize)

    def percDown(self, i):
        while (i * 2) <= self.curerntSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
                i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.curerntSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        ret = self.heapList[1]
        self.heapList[1] = self.heapList[self.curerntSize]
        self.curerntSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return ret

    def buildHeap(self, arr):
        i = len(arr) // 2
        self.curerntSize = len(arr)
        self.heapList = [0] + arr[:]
        while (i > 0):
            self.percDown(i)
            i -= 1
