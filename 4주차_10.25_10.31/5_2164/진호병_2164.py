from collections import deque

N = int(input())

NArr = deque([i for i in range(1,N+1)])

def action(arr):
    arr.popleft()
    arr.append(arr.popleft())

while len(NArr) != 1:
    action(NArr)

print(NArr[0])
