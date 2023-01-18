# 2110번 : 공유기 설치 

import sys
input = sys.stdin.readline

n, c = map(int, input().split()) # 집개수, 공유기 개수 

graph = []

for _ in range(n):
    graph.append(int(input()))

graph.sort()


start = 1
end = graph[-1] - graph[0]   # 가장 높은 숫자의 집과 낮은 숫자의 집의 차이
ans = 0

while start <= end:
    mid = (start + end) // 2  
    routerNum = 1
    router = graph[0]
    tmp = float("INF")

    for i in range(1, n):   
        if router + mid <= graph[i]:
            tmp = min(graph[i] - router, tmp)   
            routerNum += 1            
            router = graph[i]

    if routerNum < c: # 공유기 설치를 더 해야함 -> 간격을 짧게 해야 함
        end = mid - 1

    elif routerNum >= c: # 공유기 설치가 완료 or 더 많이 됨 -> 간격 늘려야 함
        start = mid + 1
        ans = max(ans, tmp)
    
print(ans)