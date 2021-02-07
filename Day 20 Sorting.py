#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swap_count=0
# Write Your Code Here
def bubble(arr):
    count_swap = 0
    for num in range(len(arr)-1,0,-1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count_swap +=1
    return count_swap

a.sort()
print("Array is sorted in "+str(bubble(a))+" swaps.")
print("First element: "+str(a[0]))
print("Last element: "+str(a[n-1]))
