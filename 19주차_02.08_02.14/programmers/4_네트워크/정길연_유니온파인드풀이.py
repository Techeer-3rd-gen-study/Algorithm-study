def findParent(parent, a):
    if parent[a] == a:
        return a
    else:
        return(findParent(parent, parent[a]))

def unionParent(parent, a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    answer = 0
    parent= [0] * (n)
    for i in range(n):
        parent[i] = i
    
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:     # 이어져있을 경우
                unionParent(parent, i, j)
    
    # 부모 종류 개수 확인
    answer = len(list(set(parent)))
                
    return answer