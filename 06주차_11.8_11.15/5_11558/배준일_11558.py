# The Game of Death

# jk = int(input()) # 주경
# T = int(input()) # testcase 숫자 
# NtoAi = [int(input()) for _ in range(T)]
# K = 0 # 희현이가 주경이를 걸리게 하고 싶을 때 불러야하는 최소 숫자

# for i in range(T):
#     if NtoAi[i] == jk: # N번이 지목한 숫자가 주경이일때
#         break
#     else:
#         K += 1

# if K == 0: # 어떤 숫자를 말해도 주경이가 걸리지 않는다.
#     print(0)
#     print()
# else:
#     print(K) # NtoAi의 인덱스가 0부터 시작이라 +1
#     print()

# 참고 : https://jinho-study.tistory.com/886
def dfs(v):
    for n in graph[v]:
        if check[n] == 0:
            check[n] = check[v]+1
            dfs(n)
            
for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        v = int(input())
        graph[i].append(v)
    check = [0]*(N+1)
    dfs(1)
    print(check[N] if check[N] > 0 else 0)