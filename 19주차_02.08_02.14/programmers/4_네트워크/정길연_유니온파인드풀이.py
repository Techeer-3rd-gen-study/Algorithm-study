# def findParent(parent, a):
#     if parent[a] == a:
#         return a
#     else:
#         return(findParent(parent, parent[a]))

# def unionParent(parent, a,b):
#     a = findParent(parent,a)
#     b = findParent(parent,b)
    
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b


# def solution(n, computers):
#     answer = 0
#     parent= [0] * (n+1)
#     for i in range(1, n+1):
#         parent[i] = i
    
#     for i in range(n):
#         for j in range(n):
#             if i == j: continue
#             if computers[i][j] == 1:     # 이어져있을 경우
#                 unionParent(parent, i+1, j+1)
    
#     # 부모 종류 개수 확인
#     answer = len(list(set(parent))) -1
                
#     return answer



# x원소의 부모 원소를 찾는 연산
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# find를 이용해 두 원소의 부모원소를 비교한 후, 더 작은 부모원소로 합해준다
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    # 입력받은 최대 n개의 조상노드, 뭉탱이가 나올 수 있다
    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i 
    
    com_list = []
    for i in range(n):
        for j in range(n):
            # 같은 숫자끼리는 본인을 뜻하는거라 항상 1
            if i == j: continue
            if computers[i][j] == 1:
                union(parent, i+1, j+1)
    
    linked = {}
    for i in range(1, len(parent)):
        v = find(parent, parent[i])
        if not v in linked:
            linked[v] = 1

    return len(linked)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
