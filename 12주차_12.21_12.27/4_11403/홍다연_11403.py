# 11403번 : 경로 찾기 

import sys
input = sys.stdin.readline

n = int(input())  # 정점의 개수 
graph = [list(map(int,input().split())) for _ in range(n)]   # 그래프 

# 플로이드 워셜
for r in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][r]==1 and graph[r][j]==1):
                graph[i][j] = 1

# *을 붙여 리스트를 언패킹 해준다. 
for x in graph:
    print(*x)

