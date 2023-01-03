# 1922번 : 네트워크 연결 

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def find(x): 
    if x == parent[x] :
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x, y = find(x), find(y)
    parent[x] = y


edges = [list(map(int,input().split())) for _ in range(m)]
edges = sorted(edges, key=lambda k: k[2])
parent = [i for i in range(0, n + 2)]
result = 0

for e in edges:
   start, end, weight = e
   if find(start) == find(end):
      continue
   else:
      result += weight
      union(start, end)

print(result)

