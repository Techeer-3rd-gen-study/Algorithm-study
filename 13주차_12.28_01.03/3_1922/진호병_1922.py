import sys
input = sys.stdin.readline
 
N = int(input())
M = int(input())
arr = []
root = [i for i in range(N+1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    arr.append([v, s, e])
 
 
def findRoot(x):
    if root[x] != x:
        root[x] = findRoot(root[x])
    return root[x]
 
 
result = 0
arr.sort()
for v, s, e in arr:
    sRoot = findRoot(s)
    eRoot = findRoot(e)
    if sRoot != eRoot:
        result += v
        if sRoot < eRoot:
            root[eRoot] = sRoot
        else:
            root[sRoot] = eRoot
 
print(result)