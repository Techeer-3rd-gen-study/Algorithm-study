# 실패, https://computer-science-student.tistory.com/662

import sys

input = sys.stdin.readline

n = int(input())  # 지방의 수
arr = list(map(int, input().split()))  # 예산 요청
m = int(input())  # 총 예산
start, end = 0, max(arr)

while start <= end:  # 이분탐색
    mid = (start + end) // 2  # 상한액 설정
    curr = 0
    for i in arr:
        if i >= mid:  # 요청한 금액이 상한액 이상이라면
            curr += mid  # 상한액 더하기
        else:  # 상한액 미만이라면
            curr += i  # 요청한 금액 더하기
    if curr <= m:  # 예산 총액이 총 예산 이하라면
        start = mid + 1
    else:  # 예산 총액이 총 예산을 초과한다면
        end = mid - 1

print(end)
    






# import sys
# input = sys.stdin.readline

# def binary_search(array, target, start, end):
#     if  start > end:
#         return None
#     mid = (start + end) //2
#     if array[mid] == target :
#         return mid
#     elif array[mid] > target : 
#         return binary_search(array, target, start, mid-1)
#     else : 
#         return binary_search(array, target, mid+1, end)
 

# n = int(input()) 

# array = list(map(int, input().split()))

# target = int(input())

# result = binary_search(array, target, 0, n-1)

# if result == None : 
#     print("원소 x")
# else : 
#     print(result + 1)