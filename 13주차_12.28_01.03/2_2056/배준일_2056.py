# 작업

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n + 1) # 진입차수
graph = [[] for _ in range(n + 1)] 
dp = [0] * (n + 1)
t = [0]

for i in range(1, n + 1):
    array = list(map(int, input().split()))
    t.append(array[0])

    if array[1] != 0:

        for j in range(2, len(array)):
            graph[array[j]].append(i)
            indegree[i] += 1

# 위상정렬
q = deque()

for i in range(1, n + 1):

    if indegree[i] == 0:
        q.append(i)
        dp[i] = t[i]


while q:
    now = q.popleft()

    for i in graph[now]:

        indegree[i] -= 1
        dp[i] = max(dp[now] + t[i], dp[i])

        if indegree[i] == 0:
            q.append(i)

print(max(dp))