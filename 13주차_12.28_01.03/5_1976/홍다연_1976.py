# 1976 : 여행 가자 

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

def bfs(ary, start, visit):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        node = q.popleft()

        for idx, item in enumerate(ary[node]):
            if item and visit[idx] == 0:
                visit[idx] = 1
                q.append(idx)

ary = []
visited = [0] * n
flag = True

for _ in range(n):
    ary.append(list(map(int, input().split())))

city = list(map(int,input().split()))
start = city[0] - 1

bfs(ary, start, visited)

for c in city:
    if visited[c - 1] == 0:
        flag = False
if flag:
    print('YES')
else:
    print('NO')

