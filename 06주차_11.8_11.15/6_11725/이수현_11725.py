# 11725 : 트리의 부모 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n + 1)]
parents = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().rstrip().split())
    # 그래프 생성
    tree[a].append(b)
    tree[b].append(a)

def dfs(start, tree, parents):
    # parents 부모 생성하고 dfs 탐색
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)

dfs(1, tree, parents)

for i in range(2, n + 1):
    print(parents[i])