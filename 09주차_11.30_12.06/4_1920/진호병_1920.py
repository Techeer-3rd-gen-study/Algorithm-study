import sys

input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))

array.sort()

M = int(input())

checkArr = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if  start > end:
        return 0
    mid = (start + end) //2
    if array[mid] == target :
        return 1
    elif array[mid] > target : 
        return binary_search(array, target, start, mid-1)
    else : 
        return binary_search(array, target, mid+1, end)
 

for target in checkArr:
    result = binary_search(array, target, 0, N-1)
    print(result)