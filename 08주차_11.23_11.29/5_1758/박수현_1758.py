import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)
sum = 0

for i in range(n):
    if arr[i] - i < 0:
        continue
    sum += (arr[i] - i)
print(sum)