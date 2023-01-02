# 1446번 : 지름길

import sys
input = sys.stdin.readline

# 지름길 개수, 고속도로 길이 
n, d = map(int, input().split())

# 지름길 그래프 입력 (start, end, long 순으로 입력된다)
graph = [list(map(int, input().split())) for _ in range(n)]

distance = [i for i in range(d + 1)]

for i in range(d + 1):
    distance[i] = min(distance[i], distance[i - 1] + 1)
    # 그래프 시작이 같은 곳에서 지름길이 더 짧을경우 지름길을 택한다
    for start, end, long in graph:
        if i == start and end <= d and distance[i] + long < distance[end] :
            distance[end] = distance[i] + long

print(distance[d])
