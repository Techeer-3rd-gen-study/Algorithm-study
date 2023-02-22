def getParent(parent, x):
    if parent[x] == x:      # 첫출 or 최상위
        return x
    else:   # 최상위 부모 찾기위해 올라감
        return getParent(parent, parent[x])

def sameParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return True
    else:
        return False
    
def unionParent(parent,a,b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:    # 작은쪽으로 부모 몰아주기
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    count = 0
    
    parent = [0] * (n+1)
    for i in range(n):
        parent[i] = i
    
    # 비용순으로 정렬
    costs. sort(key=lambda x : x[2])
    
    for cost in costs:
        # 같은 부모가 아닐경우
        if not sameParent(parent, cost[0], cost[1]):
            answer += cost[2]
            unionParent(parent, cost[0], cost[1]) # 부모 같게 해주기
            count += 1
        
        if count == (n-1): # 간선은 노드 개수 - 1개여야함
            break
    
    
    return answer