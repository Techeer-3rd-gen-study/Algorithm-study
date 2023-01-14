# 참고: https://donghak-dev.tistory.com/154

from collections import defaultdict, deque

N = int(input())
answer = [0] * (N+1)
cost = [0] * (N+1)
degree = [0] * (N+1)
Q = deque()

graph = defaultdict(list)
for i in range(1,N+1):
    temp = list(map(int, input().split()))
    cost[i] = temp[0]

    for element in temp[1:-1]:
        graph[element].append(i)
        degree[i] += 1


for i in range(1,N+1):
    if degree[i] == 0:
        Q.append(i)
        answer[i] = cost[i]

while Q:
    now = Q.popleft()
    for element in graph[now]:
        degree[element] -= 1
        answer[element] = max(answer[element], cost[element] + answer[now])

        if degree[element] == 0:
            Q.append(element)


for i in range(1, len(answer)):
    print(answer[i])
