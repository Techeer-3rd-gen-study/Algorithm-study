# 참고: https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-1717%EB%B2%88-%EC%A7%91%ED%95%A9%EC%9D%98-%ED%91%9C%ED%98%84-Python-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0

import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)] # 자기 자신을 부모로 갖는 n + 1개 집합

# 찾기 연산(같은 집합에 속하는지 확인하기 위한 함수)
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 합집합 연산(두 집합을 합치기 위한 함수)
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: # 값이 더 작은 쪽을 부모로
        parent[b] = a
    else:
        parent[a] = b
        
for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
