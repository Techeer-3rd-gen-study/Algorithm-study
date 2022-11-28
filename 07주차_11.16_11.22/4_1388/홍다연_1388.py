# 백준 1388번 : 바닥 장식 
# '-' 은 행(row)을, '|' 은 열(column)을 확인해야 한다. 

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []

# 바닥 입력
for _ in range(n) :
    graph.append(list(input()))

count = 0

# '-' 
for i in range(n) :
    check = 0
    for j in range(m) :   # 같은 줄에서 '-' 확인 
        if graph[i][j] == '-' and graph[i][j] != check :  # 이전 타일과 다른 종류 경우, +1 
                count += 1
        check = graph[i][j]

# '|'
for j in range(m) :
    check = 0
    for i in range(n):  # 같은 열에서 '|' 확인 
        if graph[i][j] == '|' and graph[i][j] != check :  # 이전 타일과 다른 종류인 경우, +1
            count += 1
        check = graph[i][j]

print(count)
