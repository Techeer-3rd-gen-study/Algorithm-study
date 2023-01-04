# 1922 : 네트워크 연결
# 크루스컬 알고리즘으로 주어진 그래프를 MST로 만들고 총 가중치 출력
# https://deep-learning-study.tistory.com/593

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input()) # 정점 수 입력 받기
M = int(input()) # 간선 수 입력 받기
parent = [0] * (N+1) # 루트 노드를 저장할 자료구조
rank = [0] * (N+1) # 정점의 rank를 저장할 자료구조
edges = [[] for i in range(M+1)] # 간선 정보를 저장할 자료구조

# parent 초기화, 자기 자신을 루트 노드로 설정
for i in range(1, N+1):
    parent[i] = i

# 간선 정보 입력 받기
for i in range(1, M+1): # 간선 수 만큼 반복
    a, b, c = map(int, input().split()) # 간선 정보 입력 (출발 정점, 도착 정점, 비용)
    edges[i].extend([c, a, b]) # 비용, 출발 정점, 도착 정점

# union find algorithm
def find(a): # a 정점의 루트 노드 탐색
    if parent[a] == a: # a가 루트 노드이면, a 반환
        return a
    p = find(parent[a]) # 루트 노드 탐색
    parent[a] = p # a의 루트 노드 갱신
    return parent[a]

def union(a, b): # a와 b 집합을 병합
    a = find(a) # a의 루트 노드 탐색
    b = find(b) # b의 루트 노드 탐색
    if a == b: # 루트 노드가 동일하면, 동일한 집합
        return
    if rank[a] > rank[b]: # rank가 낮은 집합을 rank가 높은 집합으로 병합
        parent[b] = a # 병합
    else:
        parent[a] = b # 집합 병합
        if rank[a] == rank[b]: # 두 랭크가 동일하면
            rank[b] += 1 # 랭크 +1

# 크루스컬 알고리즘
def kruskal(edges):
    edges.sort() # 비용을 기준으로 정렬
    total = 0 # 최종 비용
    MST = [] # 최소 신장 트리
    # 간선 연결
    for edge in edges:
        if not edge: # 0 번째 edge 생략
            continue
        cost, a, b = edge # 간선 정보 추출
        if find(a) != find(b): # 서로 다른 집합인 경우
            union(a,b) # a, b 병합
            total += cost # 비용 갱신
            MST.append((a,b)) # 최소 신장 트리

    return total, MST

total, MST = kruskal(edges)
print(total)