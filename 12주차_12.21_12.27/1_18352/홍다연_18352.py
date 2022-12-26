# 18352번 : 특정 거리의 도시 찾기 

from collections import deque
import sys
input = sys.stdin.readline

# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시의 번호 x 
n, m, k, x = map(int, input().split() )

graph = [ [] for _ in range(n + 1) ] 

# 도로의 연결정보 받아 graph 리스트에 저장 
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n + 1)  # 최단거리 -> 아직 방문하지 않은 도시의 거리 = -1
distance[x] = 0   # 출발 도시 

queue = deque()
queue.append(x)

while queue:
    now = queue.popleft()

    for next_node in graph[now]:
        # 방문하지 않은 도시는 최단거리 갱신 
        if distance[next_node] == -1 :
            distance[next_node] = distance[now] + 1
            queue.append(next_node)
    
check = False

for i in range(1, n + 1):
    if distance[i] == k:  # 최단거리가 k인 경우 출력후, true 체크 
        print(i)
        check = True
        
if check == False:
    print(-1)
