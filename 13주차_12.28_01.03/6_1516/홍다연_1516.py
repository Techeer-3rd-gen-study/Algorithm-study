# 1516번 : 개임 개발 
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

hour = defaultdict(int)
order = defaultdict(list)
cnt = defaultdict(int)

n = int(input())

for i in range(1,n+1):
    m = list(map(int,input().split()))
    hour[i] = m[0]
    if m[1] == -1 : 
        continue
    for j in m[1:-1] :
        order[j].append(i)
        cnt[i]+=1
        
q = []
ans = [0] * (n+1)

for i in range(1,n+1):
    if cnt[i] == 0:
        q.append(i)
        ans[i]=hour[i]

while q:
    x=q.pop()
    for y in order[x]: # y는 x 다음에 오는 작업 
        ans[y] = max(ans[y],ans[x]+hour[y])
        cnt[y] -= 1
        if cnt[y] == 0:
            q.append(y)

for i in range(1,n + 1):
    print(ans[i])
