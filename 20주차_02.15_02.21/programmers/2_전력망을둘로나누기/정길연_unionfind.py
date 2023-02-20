import copy
# copy.copy(x): x의 얕은 복사
# copy.deepcopy(x): x의 깊은 복사

def solution(n, wires):
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i
    
    # 부모가 누구인지 찾는 함수
    def findParent(parent, x):
        if parent[x] == x:
            return x
        else:
            return findParent(parent,parent[x])
        
    # 부모를 합쳐주는 함수
    def unionParent(parent, a, b):
        a = findParent(parent, a)
        b = findParent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    answer = 1e9
    for i in range(len(wires)):
        parent_cp = copy.deepcopy(parent)
        for j in range(len(wires)):     
            if i == j:  #  i번째 간선 끊기 
                continue
            a, b = wires[j]
            unionParent(parent_cp, a, b)
            
        for a,b in wires:
            parent_cp[a] = findParent(parent_cp,a)
            parent_cp[b] = findParent(parent_cp,b)
        
        # i번째 때 끊었으니, i번째의 부모노드 2개의 개수확인해서 절댓값확인
        answer = min( abs(parent_cp.count(parent_cp[wires[i][0]]) - parent_cp.count(parent_cp[wires[i][1]])), answer)
        
    return answer