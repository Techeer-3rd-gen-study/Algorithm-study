# 네트워크 연결

def find_parent(parent, x): # 특정 원소가 속한 집합 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # 두 원소가 속한 집합 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input()) # 컴퓨터 수
m = int(input()) # 선의 수

parent = [0] * (n + 1) # 부모 테이블 
edges = []
result = 0

for i in range(1, n + 1): # 부모를 자기 자신으로 초기화
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split()) # c = 비용
    edges.append((c, a, b)) # 비용순으로 정렬하기 위해 c를 첫번째 원소로 지정

edges.sort() # 비용순으로 정렬

for edge in edges:
    c, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않은 경우에만 집합에 포함
        union_parent(parent, a, b)
        result += c

print(result)