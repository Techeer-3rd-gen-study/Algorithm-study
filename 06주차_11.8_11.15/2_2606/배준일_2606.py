# 바이러스

import sys
input = sys.stdin.readline 

com_vertex = int(input()) # 컴퓨터의 수
com_edge = int(input()) # 연결된 쌍 개수
com_virus = 0 # 바이러스에 걸린 컴퓨터 수

graph = [[] for _ in range(com_vertex + 1)] # connect 저장 리스트 // 인덱스 0 은 사용 안함
visited = [False] * (com_vertex + 1) # 방문 여부 // 인덱스 0 은 사용 안함

for _ in range(com_edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global com_virus # 코드가 전역 변수에 액세스하려고 할 때 오류 발생 -> global로 전역변수 선언
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            visited[i] = True
            com_virus += 1

dfs(1)
print(com_virus)
