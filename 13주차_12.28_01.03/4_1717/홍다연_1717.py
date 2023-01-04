# 1717번 : 집합의 표현 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x) :
    if x == parent[x] :
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    a = find(a)
    b = find(b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

