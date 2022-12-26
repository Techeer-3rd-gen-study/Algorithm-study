# 1058번 : 친구
# https://velog.io/@sugenius77/%EB%B0%B1%EC%A4%80Python-1058%EB%B2%88-%EC%B9%9C%EA%B5%AC

import sys
input = sys.stdin.readline

n = int(input())  # 사람 수

graph = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range (n)]

# 플로이드 워셜
for i in range(n) :
    for j in range(n) :
        for k in range(n) :
            if j == k : 
                continue
            
            # 2-친구 인 경우 = 직접 친구 또는 한다리 건너 아는 친구 
            if graph[j][k] == 'Y' or (graph[j][i] == 'Y' and graph[i][k] == 'Y') : 
                visited[j][k] = 1

result = 0

for i in visited :
    result = max(result, sum(i))

print (result)


