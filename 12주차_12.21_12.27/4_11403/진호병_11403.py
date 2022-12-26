# 실패 https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-11403%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Floyd-Warshall
 
import sys

input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])